import unittest
from fastapi.testclient import TestClient
from task_3_main import app


class TestAPI(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)

    def test_postcode_validator(self):
        # Test postcode validation
        valid_postcodes = [
            "EC1A1BB",
            "W1A0AX",
            "M1 1AE",
            "B33 8TH",
            "CR2 6XH",
            "DN55 1PT",
            "SW1W 0NY",
        ]
        for postcode in valid_postcodes:
            response = self.client.get(f"/?input_postcode={postcode}")
            self.assertEqual(response.status_code, 200)
            self.assertTrue(response.json()['valid_postcode'])

        invalid_postcodes = [
            "EC1A1B",
            "W1A0A",
            "M1 1A",
            "B33 8T",
            "CR2 6X",
            "DN55 1P",
            "SW1W 0N",
            "B3 3",
            "CR2 6XHH"
        ]
        for postcode in invalid_postcodes:
            response = self.client.get(f"/?input_postcode={postcode}")

            if not 6 <= len(postcode) <= 9:
                self.assertEqual(response.status_code, 400)
            else:
                self.assertEqual(response.status_code, 200)
                self.assertFalse(response.json()['valid_postcode'])

    def test_postcode_formatter(self):
        # Test postcode formatting
        test_cases = [
            ("ec1a1bb", "EC1A 1BB"),
            ("W1a0ax", "W1A 0AX"),
            ("M1 1AE", "M1 1AE"),
            ("b33 8TH", "B33 8TH"),
            ("CR2 6XH", "CR2 6XH"),
            ("DN55 1PT", "DN55 1PT"),
            ("Sw1w0ny", "SW1W 0NY"),
        ]
        for postcode, expected_formatted_postcode in test_cases:
            response = self.client.get(f"/?input_postcode={postcode}")
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.json()['formatted_postcode'], expected_formatted_postcode)
