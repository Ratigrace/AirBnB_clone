#!/usr/bin/python3
"""The Amenity model test case"""
import unittest
from models.amenity import Amenity
import pycodestyle


class TestAmenity(unittest.TestCase):
    """Test Amenity model"""

    def setUp(self):
        """Test setup"""

        self.amenity = Amenity()
        self.file_path = "models/amenity.py"

    def test_init(self):
        """Test that 'name' attribute is an empty strings"""

        self.assertEqual(self.amenity.name, '')

    def test_docstrings(self):
        """Check if class docstring and attribute docstrings are present"""

        self.assertIsNotNone(Amenity.__doc__)
        self.assertIsNotNone(Amenity.name.__doc__)

    def test_pep8_conformance(self):
        """Test pep8 conformance"""

        style = pycodestyle.StyleGuide(quiet=False)
        result = style.check_files([self.file_path])
        self.assertEqual(result.total_errors, 0, "PEP8 style violations found")


if __name__ == '__main__':
    unittest.main()
