from pathlib import Path
import tempfile
import unittest
from scripts.check_docs import check_file


class CheckDocsTests(unittest.TestCase):
    def check(self, text, targets=()):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            path = root / "README.md"
            path.write_bytes(text.encode("utf-8"))
            for target in targets:
                other = root / target
                other.parent.mkdir(parents=True, exist_ok=True)
                other.write_text("ok\n", encoding="utf-8")
            return check_file(path, root)

    def test_valid_local_and_external(self):
        self.assertEqual(self.check("# Guide\n\n[Local](docs/guide.md) [Web](https://example.com)\n", ["docs/guide.md"]), [])

    def test_missing_link(self):
        self.assertTrue(any("missing local target" in x for x in self.check("[bad](missing.md)\n")))

    def test_absolute_repository_link(self):
        self.assertEqual(self.check("[Guide](https://github.com/NOMAD-DnA/.github/blob/main/docs/guide.md)\n", ["docs/guide.md"]), [])

    def test_unclosed_fence(self):
        self.assertTrue(any("unclosed" in x for x in self.check("```bash\ngit status\n")))

    def test_code_example_ignored(self):
        self.assertEqual(self.check("```markdown\n[x](missing.md)\n```\n"), [])

    def test_conflict_markers(self):
        self.assertTrue(any("conflict" in x for x in self.check("<<<<<<< HEAD\n")))

    def test_escape(self):
        self.assertTrue(any("escapes" in x for x in self.check("[bad](../outside.md)\n")))

    def test_heading_and_eof(self):
        errors = self.check("#Bad")
        self.assertTrue(any("heading" in x for x in errors))
        self.assertTrue(any("newline" in x for x in errors))

    def test_crlf(self):
        self.assertTrue(any("LF line endings" in x for x in self.check("# Guide\r\n")))


if __name__ == "__main__":
    unittest.main()
