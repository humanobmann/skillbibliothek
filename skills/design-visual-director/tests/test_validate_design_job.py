"""Focused regression tests for Canva routing and design release gates."""
import importlib.util
import unittest
from pathlib import Path

FILE = Path(__file__).resolve().parents[1] / "scripts" / "validate_design_job.py"
spec = importlib.util.spec_from_file_location("validate_design_job", FILE)
dv = importlib.util.module_from_spec(spec)
spec.loader.exec_module(dv)


def sample():
    return {
        "campaign_id": "pilot-kw46",
        "project_scope": "parliamentary",
        "canva_account": "SPÖ",
        "template_source_account": "SPÖ",
        "output": {"type": "canva_native", "format": "feed_4_5", "width_px": 1080, "height_px": 1350},
        "assets": {"logo": {"origin": "approved_original"}, "person": {"real_person": True, "ai_replaced": False}},
        "content": {"factual_claims": True, "source_refs": ["Official source"]},
        "qa": {"text_exact_checked": True, "dimensions_checked": True, "brand_checked": True,
               "safe_area_checked": True, "render_checked": True, "person_identity_checked": True,
               "sources_checked": True},
        "release": {"status": "Final", "human_approved": True, "automatic_publication": False},
    }


class DesignV5Tests(unittest.TestCase):
    def fail(self, field, text):
        result = dv.inspect(field)
        self.assertFalse(result["pass"], result)
        self.assertTrue(any(text in e for e in result["errors"]), result)

    def test_valid(self):
        self.assertTrue(dv.inspect(sample())["pass"])

    def test_party_wrong_account(self):
        j = sample(); j["canva_account"] = "Peter"; self.fail(j, "conflicts")

    def test_personal_wrong_account(self):
        j = sample(); j["project_scope"] = "personal"; self.fail(j, "conflicts")

    def test_ngo_wrong_account(self):
        j = sample(); j["project_scope"] = "ngo"; self.fail(j, "conflicts")

    def test_cross_account_source(self):
        j = sample(); j["template_source_account"] = "Peter"; self.fail(j, "Cross-account")

    def test_html_forbidden(self):
        j = sample(); j["output"]["type"] = "html_iframe"; self.fail(j, "no HTML")

    def test_wrong_feed_dimensions(self):
        j = sample(); j["output"]["height_px"] = 1200; self.fail(j, "requires 1080 x 1350")

    def test_ai_logo(self):
        j = sample(); j["assets"]["logo"]["origin"] = "AI"; self.fail(j, "approved original")

    def test_person_replaced(self):
        j = sample(); j["assets"]["person"]["ai_replaced"] = True; self.fail(j, "real person")

    def test_no_automatic_posting(self):
        j = sample(); j["release"]["automatic_publication"] = True; self.fail(j, "Automatic publication")

    def test_human_approval_required(self):
        j = sample(); j["release"]["human_approved"] = False; self.fail(j, "human approval")

    def test_render_check(self):
        j = sample(); j["qa"]["render_checked"] = False; self.fail(j, "render_checked")

    def test_sources(self):
        j = sample(); j["content"]["source_refs"] = []; self.fail(j, "requires sources")

    def test_unverified_editable_layers(self):
        j = sample(); j["output"]["type"] = "image_to_design_experimental"; self.fail(j, "editable layers")

    def test_verified_layers(self):
        j = sample(); j["output"]["type"] = "image_to_design_experimental"
        j["qa"]["editable_layers_checked"] = True; self.assertTrue(dv.inspect(j)["pass"])

    def test_draft_allowed(self):
        j = sample(); j["release"]["status"] = "Entwurf"; j["release"]["human_approved"] = False
        j["qa"] = {}; self.assertTrue(dv.inspect(j)["pass"])

    def test_story(self):
        j = sample(); j["output"].update(format="story_9_16", height_px=1920)
        self.assertTrue(dv.inspect(j)["pass"])

    def test_non_object(self):
        self.assertFalse(dv.inspect([])["pass"])


if __name__ == "__main__":
    unittest.main()
