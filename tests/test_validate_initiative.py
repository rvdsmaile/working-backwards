from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path
import tempfile
import unittest


SCRIPT = Path(__file__).parents[1] / ".agents/working-backwards/scripts/validate_initiative.py"
SPEC = spec_from_file_location("validate_initiative", SCRIPT)
MODULE = module_from_spec(SPEC)
assert SPEC and SPEC.loader
SPEC.loader.exec_module(MODULE)

TECHNICAL_SCRIPT = Path(__file__).parents[1] / ".agents/working-backwards/scripts/validate_technical_artifacts.py"
TECHNICAL_SPEC = spec_from_file_location("validate_technical_artifacts", TECHNICAL_SCRIPT)
TECHNICAL_MODULE = module_from_spec(TECHNICAL_SPEC)
assert TECHNICAL_SPEC and TECHNICAL_SPEC.loader
TECHNICAL_SPEC.loader.exec_module(TECHNICAL_MODULE)


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

    def test_technical_delivery_requires_handoff(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.write(root, "initiative.md", "## Phase\n\ndrafting\n")
            self.write(root, "decision-log.md")
            self.write(root, "announcement.md")
            self.write(root, "faq.md")
            self.assertIn(
                "technical delivery requires handoff phase, found drafting",
                MODULE.validate(root, require_handoff=True),
            )

    def test_validates_technical_prd_template(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "technical-prd.md"
            path.write_text("\n".join(TECHNICAL_MODULE.REQUIRED_HEADINGS["prd"]), encoding="utf-8")
            self.assertEqual(TECHNICAL_MODULE.validate(path, "prd"), [])

    def test_reports_missing_issue_breakdown_sections(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "issues.md"
            path.write_text("## Source PRD\n", encoding="utf-8")
            self.assertEqual(
                TECHNICAL_MODULE.validate(path, "issues"),
                [
                    "missing required heading: ## Publication status",
                    "missing required heading: ## Issues",
                ],
            )

    def test_validates_complete_vertical_issue_slice(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "issues.md"
            path.write_text(
                "\n".join(
                    (
                        "## Source PRD",
                        "## Publication status",
                        "## Issues",
                        "### 1. Create a complete path",
                        "- Type: AFK",
                        "- Blocked by: None — can start immediately",
                        "#### What to build",
                        "#### Acceptance criteria",
                        "#### Verification",
                    ),
                ),
                encoding="utf-8",
            )
            self.assertEqual(TECHNICAL_MODULE.validate(path, "issues"), [])


if __name__ == "__main__":
    unittest.main()
