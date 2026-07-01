import os
import sys
import unittest

from fastapi.testclient import TestClient

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
from app import app


class ActivityTests(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)

    def test_github_skills_activity_is_available(self):
        response = self.client.get("/activities")

        self.assertEqual(response.status_code, 200)
        self.assertIn("GitHub Skills", response.json())


if __name__ == "__main__":
    unittest.main()
