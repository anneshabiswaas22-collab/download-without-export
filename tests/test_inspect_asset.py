"""Offline tests for the light metadata inspector."""
import tempfile
import unittest
from pathlib import Path
import sys
import struct

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from inspect_asset import inspect, sniff_type


class AssetInspectTests(unittest.TestCase):
    def write_and_inspect(self, suffix, data):
        with tempfile.TemporaryDirectory() as temporary:
            path = Path(temporary) / ("asset" + suffix)
            path.write_bytes(data)
            return inspect(path)

    def test_valid_glb_header(self):
        data = b"glTF" + struct.pack("<II", 2, 12)
        output = self.write_and_inspect(".glb", data)
        self.assertEqual(output["status"], "recognized_header")
        self.assertEqual(output["recognized_header_type"], "glb")
        self.assertEqual(len(output["sha256"]), 64)
        self.assertEqual(output["blender_import"], "not_tested")

    def test_bad_glb_length(self):
        data = b"glTF" + struct.pack("<II", 2, 50)
        self.assertEqual(self.write_and_inspect(".glb", data)["status"], "invalid_glb_header")

    def test_html_masquerading_as_fbx(self):
        output = self.write_and_inspect(".fbx", b"<!doctype html><html>Error</html>")
        self.assertEqual(output["status"], "invalid_html_or_error_document")

    def test_fbx_magic(self):
        output = self.write_and_inspect(".fbx", b"Kaydara FBX Binary  \x00\x1a\x00" + b"x" * 80)
        self.assertEqual(output["status"], "recognized_header")

    def test_spz_remains_unverified(self):
        output = self.write_and_inspect(".spz", b"UNVERIFIED" * 100)
        self.assertEqual(output["status"], "unverified_header")
        self.assertTrue(any("SPZ" in warning for warning in output["warnings"]))

    def test_extension_mismatch(self):
        output = self.write_and_inspect(".fbx", b"ply\nformat ascii 1.0\nend_header\n")
        self.assertEqual(output["status"], "extension_header_mismatch")

    def test_blank_file(self):
        self.assertEqual(self.write_and_inspect(".glb", b"")["status"], "invalid_empty_file")

    def test_obj_text_heuristic(self):
        self.assertEqual(sniff_type(b"# object\nv 1.0 2.0 3.0\nf 1 2 3\n"), "obj")


if __name__ == "__main__":
    unittest.main()
