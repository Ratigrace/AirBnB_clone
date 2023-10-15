#!/usr/bin/python3
"""The City model test case"""
import unittest
from models.city import City
import pycodestyle

class TestCity(unittest.TestCase):
    def setUp(self):
        self.city = City()
        self.file_path = "models/city.py"

    def test_init(self):
        # Test that 'state_id' and 'name' attributes are empty strings
        self.assertEqual(self.city.state_id, '')
        self.assertEqual(self.city.name, '')

    def test_docstrings(self):
        # Check if class docstring and attributes docstrings are present
        self.assertIsNotNone(City.__doc__)
        self.assertIsNotNone(City.state_id.__doc__)
        self.assertIsNotNone(City.name.__doc__)

    def test_pep8_conformance(self):
        style = pycodestyle.StyleGuide(quiet=False)
        result = style.check_files([self.file_path])
        self.assertEqual(result.total_errors, 0, "PEP8 style violations found")

if __name__ == '__main__':
    unittest.main()