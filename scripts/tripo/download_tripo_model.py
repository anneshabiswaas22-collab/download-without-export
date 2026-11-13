#!/usr/bin/env python3
"""Download this exact public Tripo model using its fresh Nuxt page data.

Requires curl and Python 3.8+. Does not use Tripo's Export button or APIs.
Run: python download_tripo_model.py
"""

import json
import os
import re
import shutil
import subprocess
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit

MODEL_ID = "e3bca070-3984-4aa3-8d54-1192acc9da1e"
PAGE_URL = (
    f"https://studio.tripo3d.ai/3d-model/{MODEL_ID}"
    ""
)
TARGET_DIR = Path(__file__).resolve().parent
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/132.0 Safari/537.36"


class NuxtDataParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.inside = False
        self.scripts = []
        self.current = []

    def handle_starttag(self, tag, attrs):
        if tag == "script" and dict(attrs).get("id") == "__NUXT_DATA__":
            self.inside = True
            self.current = []

    def handle_data(self, data):
        if self.inside:
            self.current.append(data)

    def handle_endtag(self, tag):
        if tag == "script" and self.inside:
            self.scripts.append("".join(self.current))
            self.inside = False


def curl_bytes(url):
    if not shutil.which("curl"):
        raise RuntimeError("curl is not installed. Please install curl first.")
    cmd = [
        "curl", "-fLsS", "--retry", "2", "--connect-timeout", "20",
        "-A", UA, "--compressed", url,
    ]
    proc = subprocess.run(cmd, capture_output=True, check=False)
    if proc.returncode:
        raise RuntimeError(
            f"curl could not retrieve the public page (exit {proc.returncode}): "
            + proc.stderr.decode("utf-8", "replace").strip()
        )
    return proc.stdout


def parse_nuxt(html_bytes):
    parser = NuxtDataParser()
    parser.feed(html_bytes.decode("utf-8", "replace"))
    if not parser.scripts:
        raise RuntimeError("The fresh page has no __NUXT_DATA__ script (page format or access may have changed).")
    entries = json.loads(parser.scripts[0])
    if not isinstance(entries, list):
        raise RuntimeError("Nuxt data is not an indexed array.")
    return entries


class Resolver:
    """Resolve integer references in Nuxt/devalue's indexed array."""

    def __init__(self, data):
        self.data = data

    def deref(self, obj, depth=0, seen=frozenset()):
        if depth > 30:
            return None
        if isinstance(obj, int) and not isinstance(obj, bool):
            if obj < 0 or obj >= len(self.data) or obj in seen:
                return None
            return self.deref(self.data[obj], depth + 1, seen | {obj})
        if isinstance(obj, list) and len(obj) >= 2 and isinstance(obj[0], str):
            if obj[0] in ("Reactive", "Ref", "ShallowRef", "Readonly", "ShallowReactive"):
                return self.deref(obj[1], depth + 1, seen)
        return obj

    def text(self, value):
        val = self.deref(value)
        return val if isinstance(val, str) else None

    def obj(self, value):
        val = self.deref(value)
        return val if isinstance(val, dict) else None

    def url_in_record(self, record):
        # Only inspect this exact record and its own model field; never
        # select a URL from unrelated or recommended project records.
        for key in ("model_url", "modelUrl"):
            url = self.text(record.get(key)) if key in record else None
            if url and url.startswith(("https://", "http://")):
                return url
        model = self.obj(record.get("model")) if "model" in record else None
        if model:
            for key in ("modelUrl", "model_url"):
                url = self.text(model.get(key)) if key in model else None
                if url and url.startswith(("https://", "http://")):
                    return url
        return None


def find_exact_url(data):
    r = Resolver(data)
    matching = []
    # Inspect the actual indexed records, not hardcoded array offsets.
    for i, item in enumerate(data):
        if not isinstance(item, dict):
            continue
        if r.text(item.get("id")) == MODEL_ID or r.text(item.get("itemId")) == MODEL_ID:
            matching.append((i, item))
    if not matching:
        raise RuntimeError(f"No Nuxt record with id or itemId equal to {MODEL_ID} was found.")
    urls = [r.url_in_record(rec) for _, rec in matching]
    urls = list(dict.fromkeys(u for u in urls if u))
    if not urls:
        raise RuntimeError(
            f"Found {len(matching)} matching project record(s), but none provided model_url or model.modelUrl. "
            "The public page may not expose a downloadable file."
        )
    if len(urls) > 1:
        raise RuntimeError("The exact project exposed multiple different file URLs; refusing to choose arbitrarily.")
    return urls[0]


def model_extension(url):
    path = urlsplit(url).path.lower()
    for ext in (".fbx", ".glb", ".gltf", ".obj", ".zip"):
        if path.endswith(ext):
            return ext
    return ".fbx"  # The public page previously supplied an FBX.


def check_file(filename):
    size = filename.stat().st_size
    with filename.open("rb") as fp:
        head = fp.read(8192)
    stripped = head.lstrip().lower()
    if size < 1024:
        raise RuntimeError(f"File is only {size} bytes, unlikely to be a usable 3D model.")
    if stripped.startswith((b"<!doctype html", b"<html", b"<?xml")) or b"<html" in stripped[:1000]:
        raise RuntimeError("The response was HTML/XML, not a 3D model (signed URL may have expired).")
    actual_name = filename.name.lower()
    if actual_name.endswith(".partial"):
        actual_name = actual_name[:-len(".partial")]
    suffix = Path(actual_name).suffix
    if suffix == ".fbx":
        if not (head.startswith(b"Kaydara FBX Binary") or b"FBXHeaderExtension" in head or stripped.startswith(b"; fbx")):
            raise RuntimeError("Downloaded file lacks a recognizable FBX header.")
    if suffix == ".glb" and not head.startswith(b"glTF"):
        raise RuntimeError("Downloaded file lacks the GLB magic header.")
    if suffix == ".zip" and not head.startswith(b"PK\x03\x04"):
        raise RuntimeError("Downloaded file lacks the ZIP magic header.")
    return size


def blender_verify(path):
    executable = shutil.which("blender")
    if not executable or path.suffix.lower() != ".fbx":
        print("Blender not found or file is not FBX; skipping optional Blender import test.")
        return
    helper = TARGET_DIR / "_tripo_blender_verify.py"
    helper.write_text(
        "import bpy, sys\n"
        "filename = sys.argv[-1]\n"
        "bpy.ops.object.select_all(action='SELECT')\n"
        "bpy.ops.object.delete(use_global=False)\n"
        "try:\n"
        "    bpy.ops.import_scene.fbx(filepath=filename)\n"
        "except AttributeError:\n"
        "    bpy.ops.wm.fbx_import(filepath=filename)\n"
        "mesh = [o for o in bpy.data.objects if o.type == 'MESH']\n"
        "images = list(bpy.data.images)\n"
        "print(f'TRIPO_VERIFY mesh_objects={len(mesh)} materials={len(bpy.data.materials)} images={len(images)}')\n"
        "assert len(mesh) > 0, 'No mesh objects in imported model'\n",
        encoding="utf-8",
    )
    try:
        proc = subprocess.run(
            [executable, "--background", "--python", str(helper), "--", str(path)],
            capture_output=True, text=True, timeout=180,
        )
        for line in (proc.stdout + "\n" + proc.stderr).splitlines():
            if "TRIPO_VERIFY" in line:
                print(line)
        if proc.returncode:
            print("Blender verification was unsuccessful; file header was verified separately.")
    except (OSError, subprocess.TimeoutExpired) as exc:
        print("Blender check unavailable:", exc)
    finally:
        helper.unlink(missing_ok=True)


def main():
    print("Fetching a fresh Tripo public page using curl...")
    page = curl_bytes(PAGE_URL)
    data = parse_nuxt(page)
    print(f"Parsed Nuxt data ({len(data)} indexed entries).")
    url = find_exact_url(data)
    path = TARGET_DIR / f"tripo_{MODEL_ID}{model_extension(url)}"
    tmp = path.with_name(path.name + ".partial")
    print("Found a model file URL belonging to the exact requested ID.")
    print("Downloading it with curl -fL (including all original query parameters)...")
    cmd = [
        "curl", "-fL", "--retry", "2", "--connect-timeout", "25",
        "-A", UA, "--compressed", url, "-o", str(tmp),
    ]
    proc = subprocess.run(cmd, check=False)
    if proc.returncode:
        tmp.unlink(missing_ok=True)
        raise RuntimeError(f"The model URL download failed (curl exit {proc.returncode}; possible expired or restricted link).")
    try:
        size = check_file(tmp)
    except Exception:
        tmp.unlink(missing_ok=True)
        raise
    tmp.replace(path)
    print(f"Verified 3D file header and file size ({size:,} bytes).")
    print("Saved:", path)
    blender_verify(path)


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        print("DOWNLOAD FAILED:", exc, file=sys.stderr)
        sys.exit(1)