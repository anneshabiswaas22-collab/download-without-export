#!/usr/bin/env python3
"""Offline, dependency-free lightweight identification and hashing of 3D assets.

Not a geometry validator, Blender import test, or DRM/access workaround.
"""
import argparse
import hashlib
import json
import struct
import sys
from pathlib import Path


EXTENSION_TYPES = {
    ".fbx": "fbx", ".glb": "glb", ".gltf": "gltf", ".obj": "obj",
    ".ply": "ply", ".spz": "spz", ".blend": "blend", ".zip": "zip",
    ".usdz": "zip",
}


def sniff_type(head: bytes) -> str | None:
    if not head:
        return None
    stripped = head.lstrip()
    lower = stripped[:1024].lower()
    if lower.startswith((b"<!doctype html", b"<html", b"<?xml", b"{\"error\"", b"{\"message\"")) or b"<html" in lower:
        return "http_error_document"
    if head.startswith(b"glTF"):
        return "glb"
    if head.startswith(b"Kaydara FBX Binary") or stripped.startswith(b"; FBX") or b"FBXHeaderExtension" in head:
        return "fbx"
    if head.startswith((b"ply\n", b"ply\r\n")):
        return "ply"
    if head.startswith(b"BLENDER"):
        return "blend"
    if head.startswith(b"PK\x03\x04"):
        return "zip"
    if stripped.startswith(b"{"):
        try:
            data = json.loads(stripped.decode("utf-8"))
            if isinstance(data, dict) and isinstance(data.get("asset"), dict) and "version" in data["asset"]:
                return "gltf"
        except (UnicodeDecodeError, json.JSONDecodeError):
            pass
    # OBJ is plain text without a fixed magic signature: heuristic, not proof.
    lines = stripped[:4096].splitlines()
    if any(line.startswith((b"v ", b"f ", b"vn ", b"vt ")) for line in lines):
        return "obj"
    return None


def inspect(path: Path) -> dict:
    path = Path(path).expanduser().resolve(strict=True)
    if not path.is_file():
        raise ValueError("Not a regular file")
    size = path.stat().st_size
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        head = handle.read(8192)
        digest.update(head)
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    expected = EXTENSION_TYPES.get(path.suffix.lower(), "unknown")
    found = sniff_type(head)
    warnings = []
    checks = []
    if size == 0:
        status = "invalid_empty_file"
    elif found == "http_error_document":
        status = "invalid_html_or_error_document"
    elif found:
        status = "recognized_header"
        if expected != "unknown" and expected != found:
            status = "extension_header_mismatch"
            warnings.append("File extension disagrees with the recognizable header.")
    else:
        status = "unverified_header"
        warnings.append("No recognized header; NOT evidence this is a valid 3D asset.")
    if expected == "spz":
        warnings.append("SPZ requires a dedicated format parser; extension alone does not verify a Gaussian splat.")
    if found == "glb" and len(head) >= 12:
        version, embedded_length = struct.unpack("<II", head[4:12])
        checks.append({"check": "glb_version", "value": version})
        checks.append({"check": "glb_declared_length", "value": embedded_length})
        if embedded_length != size or version != 2:
            status = "invalid_glb_header"
            warnings.append("GLB version/declared size does not match an expected GLB 2.0 file.")
    warnings.append("Header/hash inspection does not confirm mesh geometry, UVs, textures, rigging or Blender compatibility.")
    return {
        "path": str(path), "size_bytes": size,
        "sha256": digest.hexdigest(), "extension_type": expected,
        "recognized_header_type": found, "status": status,
        "checks": checks, "warnings": warnings,
        "blender_import": "not_tested",
    }


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("file", type=Path, help="Local asset to inspect (no network)")
    parser.add_argument("--strict", action="store_true", help="Exit nonzero for unknown/unverified headers too")
    args = parser.parse_args(argv)
    try:
        result = inspect(args.file)
    except (OSError, ValueError) as exc:
        print(json.dumps({"status": "failed", "error": str(exc)}), file=sys.stderr)
        return 2
    print(json.dumps(result, indent=2))
    rejected = {"invalid_empty_file", "invalid_html_or_error_document", "extension_header_mismatch", "invalid_glb_header"}
    if result["status"] in rejected or (args.strict and result["status"] != "recognized_header"):
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
