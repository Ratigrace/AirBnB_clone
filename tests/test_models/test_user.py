#!/usr/bin/python3
"""The User model test case"""
import unittest
from models.user import User
import pycodestyle


class TestUser(unittest.TestCase):
    """Test the User model"""

    def setUp(self):
        """Test setup"""

        self.user = User()
        self.file_path = "models/user.py"

    def test_init(self):
        """Test that attributes are initialized correctly"""

        self.assertEqual(self.user.email, '')
        self.assertEqual(self.user.password, '')
        self.assertEqual(self.user.first_name, '')
        self.assertEqual(self.user.last_name, '')

    def test_docstrings(self):
        """Check if class docstring and attributes docstrings are present"""

        self.assertIsNotNone(User.__doc__)
        self.assertIsNotNone(User.email.__doc__)
        self.assertIsNotNone(User.password.__doc__)
        self.assertIsNotNone(User.first_name.__doc__)
        self.assertIsNotNone(User.last_name.__doc__)

    def test_pep8_conformance(self):
        """Test for pep8 conformance"""

        style = pycodestyle.StyleGuide(quiet=False)
        result = style.check_files([self.file_path])
        self.assertEqual(result.total_errors, 0, "PEP8 style violations found")


if __name__ == '__main__':
    unittest.main()
