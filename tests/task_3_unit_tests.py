import unittest
from task_3.services.ukpostcode import UKPostcode


class TestUKPostcode(unittest.TestCase):
    def test_valid_postcodes(self):
        # Test some valid postcodes
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
            uk_postcode = UKPostcode(postcode)
            self.assertTrue(uk_postcode.postcode_validator())

    def test_invalid_postcodes(self):
        # Test some invalid postcodes
        invalid_postcodes = [
            "EC1A1B",
            "W1A0A",
            "M1 1A",
            "B33 8T",
            "CR2 6X",
            "DN55 1P",
            "SW1W 0N",
            "B3 3",
            "CR2 6XHH",
        ]
        for postcode in invalid_postcodes:
            uk_postcode = UKPostcode(postcode)
            self.assertFalse(uk_postcode.postcode_validator())

    def test_formatting(self):
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
            uk_postcode = UKPostcode(postcode)
            self.assertEqual(uk_postcode.postcode_formatter()['Postcode'], expected_formatted_postcode)
