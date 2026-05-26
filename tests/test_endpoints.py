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

EXPECTED_TEXT_CONDITIONS = {
    "eUprava": "[BODY] == pat(*eUprava*)",
    "Welcome to Serbia": "[BODY] == pat(*Welcome to Serbia*)",
    "eKatastar": "[BODY] == pat(*eKatastarPublic*)",
    "data.gov.rs": "[BODY] == pat(*DATA.GOV.RS*)",
}


def load_endpoint_config():
    endpoints = {}
    current_endpoint = None
    in_conditions = False

    for line in CONFIG.read_text(encoding="utf-8").splitlines():
        if line.startswith("  - name: "):
            name = line.removeprefix("  - name: ")
            current_endpoint = {"name": name, "conditions": []}
            endpoints[name] = current_endpoint
            in_conditions = False
            continue

        if current_endpoint is None:
            continue

        if line.startswith("    url: "):
            current_endpoint["url"] = line.removeprefix("    url: ")
            in_conditions = False
            continue

        if line == "    conditions:":
            in_conditions = True
            continue

        if in_conditions and line.startswith('      - "'):
            current_endpoint["conditions"].append(line.strip().removeprefix("- ").strip('"'))
            continue

        if line and not line.startswith("      "):
            in_conditions = False

    return endpoints


class EndpointConfigTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.endpoints = load_endpoint_config()

    def test_required_endpoints_are_configured(self):
        for name, url in REQUIRED_ENDPOINTS.items():
            self.assertIn(name, self.endpoints)
            self.assertEqual(self.endpoints[name]["url"], url)

    def test_each_endpoint_has_status_latency_and_tls_assertions(self):
        for name, endpoint in self.endpoints.items():
            with self.subTest(endpoint=name):
                conditions = endpoint["conditions"]

                self.assertIn("[STATUS] == 200", conditions)
                self.assertTrue(
                    any(condition.startswith("[RESPONSE_TIME] < ") for condition in conditions),
                    conditions,
                )
                self.assertIn("[CERTIFICATE_EXPIRATION] > 168h", conditions)

    def test_expected_text_checks_are_limited_to_stable_public_markers(self):
        for name, condition in EXPECTED_TEXT_CONDITIONS.items():
            self.assertIn(condition, self.endpoints[name]["conditions"])

        configured_text_conditions = {
            endpoint["name"]: condition
            for endpoint in self.endpoints.values()
            for condition in endpoint["conditions"]
            if condition.startswith("[BODY]")
        }

        self.assertEqual(configured_text_conditions, EXPECTED_TEXT_CONDITIONS)

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
