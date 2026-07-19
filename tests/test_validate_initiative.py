from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path
import tempfile
import unittest


SCRIPT = Path(__file__).parents[1] / ".agents/working-backwards/scripts/validate_initiative.py"
SPEC = spec_from_file_location("validate_initiative", SCRIPT)
MODULE = module_from_spec(SPEC)
assert SPEC and SPEC.loader
SPEC.loader.exec_module(MODULE)


class ValidateInitiativeTests(unittest.TestCase):
    def write(self, root, name, text="# document\n"):
        (root / name).write_text(text, encoding="utf-8")

    def handoff_files(self, root, critique):
        self.write(root, "initiative.md", "# Initiative\n\n## Phase\n\nhandoff\n")
        for name in ("decision-log.md", "announcement.md", "faq.md", "product-brief.md", "build-plan.md"):
            self.write(root, name)
        self.write(root, "critique.md", critique)

    def test_accepts_complete_handoff_without_internal_faq(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.handoff_files(root, "| customer | clear | critical | team | resolved | fixed |\n")
            self.assertEqual(MODULE.validate(root), [])

    def test_reports_missing_artifact(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.write(root, "initiative.md", "## Phase\n\ndrafting\n")
            self.write(root, "decision-log.md")
            self.assertIn("missing announcement.md required for drafting", MODULE.validate(root))

    def test_reports_invalid_phase(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.write(root, "initiative.md", "## Phase\n\nlaunch\n")
            self.assertEqual(MODULE.validate(root), ["invalid phase: launch"])

    def test_blocks_open_critical_finding(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.handoff_files(root, "| delivery | no owner | critical | team | open | |\n")
            self.assertTrue(any("unresolved critical finding" in error for error in MODULE.validate(root)))


if __name__ == "__main__":
    unittest.main()
