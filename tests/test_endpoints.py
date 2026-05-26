from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
CONFIG = ROOT / "config" / "config.yaml"
SERVICES_DOC = ROOT / "docs" / "services.md"

REQUIRED_ENDPOINTS = {
    "eUprava": "https://euprava.gov.rs/",
    "eID.gov.rs": "https://eid.gov.rs/",
    "Welcome to Serbia": "https://welcometoserbia.gov.rs/",
    "ePorezi": "https://eporezi.purs.gov.rs/",
    "APR": "https://www.apr.gov.rs/",
    "LPA": "https://lpa.gov.rs/jisportal/homepage",
    "eKatastar": "https://katastar.rgz.gov.rs/eKatastarPublic/",
    "data.gov.rs": "https://data.gov.rs/",
}


class EndpointConfigTest(unittest.TestCase):
    def test_required_endpoints_are_configured(self):
        config = CONFIG.read_text(encoding="utf-8")

        for name, url in REQUIRED_ENDPOINTS.items():
            self.assertIn(f"name: {name}", config)
            self.assertIn(f"url: {url}", config)

        self.assertEqual(config.count('    conditions:\n      - "[STATUS] == 200"'), len(REQUIRED_ENDPOINTS))

    def test_services_document_covers_selection_and_rejections(self):
        services_doc = SERVICES_DOC.read_text(encoding="utf-8")

        self.assertIn("https://www.srb.guide/", services_doc)
        self.assertIn("No additional SRB.GUIDE candidates were added", services_doc)
        self.assertIn("## Rejected Candidates", services_doc)

        for name, url in REQUIRED_ENDPOINTS.items():
            self.assertIn(name, services_doc)
            self.assertIn(url, services_doc)

        for rejected in (
            "registracija.eid.gov.rs",
            "ePorezi authenticated pages",
            "APR online application flows",
            "efaktura.mfin.gov.rs",
            "SRB.GUIDE calculators",
            "PIO and health-card related pages",
        ):
            self.assertIn(rejected, services_doc)


if __name__ == "__main__":
    unittest.main()
