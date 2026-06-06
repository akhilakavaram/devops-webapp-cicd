import os
import sys
import unittest


sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app.main import health_payload, homepage_html, readiness_payload, version_payload


class AppTests(unittest.TestCase):
    def test_health_payload_contains_ok_status(self):
        payload = health_payload()

        self.assertEqual(payload["status"], "ok")
        self.assertIn("service", payload)
        self.assertIn("version", payload)
        self.assertIn("environment", payload)

    def test_version_payload_contains_service_metadata(self):
        payload = version_payload()

        self.assertEqual(payload["service"], "DevOps Starter App")
        self.assertEqual(payload["version"], "1.0.0")

    def test_readiness_payload_reports_ready(self):
        payload = readiness_payload()

        self.assertTrue(payload["ready"])
        self.assertEqual(payload["service"], "DevOps Starter App")
        self.assertEqual(payload["environment"], "local")

    def test_homepage_mentions_devops_project(self):
        html = homepage_html()

        self.assertIn("first DevOps project", html)
        self.assertIn("/health", html)
        self.assertIn("/ready", html)


if __name__ == "__main__":
    unittest.main()
