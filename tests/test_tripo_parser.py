"""No-network unit tests of recovered Tripo Nuxt indexed lookup."""
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts" / "tripo"))
from download_tripo_model import MODEL_ID, parse_nuxt, find_exact_url, model_extension


class TripoNuxtTests(unittest.TestCase):
    def test_parse_nuxt(self):
        arr = parse_nuxt(b'<html><script id="__NUXT_DATA__" type="application/json">[{"id":1},"abc"]</script></html>')
        self.assertEqual(arr[0]["id"], 1)

    def test_exact_record_excludes_related(self):
        entries = [
            {"id": 2, "model_url": 3},
            {"itemId": 4, "model": 5},
            "some-other-model",
            "https://example.org/WRONG.fbx",
            MODEL_ID,
            {"modelUrl": 6},
            "https://example.org/CORRECT.fbx?signature=ABCD",
        ]
        self.assertEqual(find_exact_url(entries), "https://example.org/CORRECT.fbx?signature=ABCD")

    def test_missing_exact_id_fails(self):
        with self.assertRaisesRegex(RuntimeError, "No Nuxt record"):
            find_exact_url([{"id": 1, "model_url": 2}, "other-id", "https://example.org/wrong.fbx"])

    def test_ambiguous_exact_id_fails(self):
        entries = [
            {"id": 2, "model_url": 3},
            {"id": 2, "model_url": 4},
            MODEL_ID,
            "https://example.org/one.fbx",
            "https://example.org/two.fbx",
        ]
        with self.assertRaisesRegex(RuntimeError, "multiple different"):
            find_exact_url(entries)

    def test_extension_path_ignores_signed_query(self):
        self.assertEqual(model_extension("https://example.org/x.glb?expires=7"), ".glb")


if __name__ == "__main__":
    unittest.main()
