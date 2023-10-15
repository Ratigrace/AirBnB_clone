#!/usr/bin/python3
"""The State model test case"""
import unittest
from models.state import State
import pycodestyle


class TestState(unittest.TestCase):
    """Test the State model"""

    def setUp(self):
        """Setup the test"""

        self.State = State()
        self.file_path = "models/state.py"

    def test_init(self):
        """Test that 'name' attribute is an empty strings"""

        self.assertEqual(self.State.name, '')

    def test_docstrings(self):
        """Check if class docstring and attribute docstrings are present"""

        self.assertIsNotNone(State.__doc__)
        self.assertIsNotNone(State.name.__doc__)

    def test_pep8_conformance(self):
        """Test for pep8 conformance"""

        style = pycodestyle.StyleGuide(quiet=False)
        result = style.check_files([self.file_path])
        self.assertEqual(result.total_errors, 0, "PEP8 style violations found")


if __name__ == '__main__':
    unittest.main()
