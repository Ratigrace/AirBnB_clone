#!/usr/bin/python3
"""The Review model test case"""
import unittest
from models.review import Review
import pycodestyle

class TestReview(unittest.TestCase):
    def setUp(self):
        self.review = Review()
        self.file_path = "models/review.py"

    def test_init(self):
        # Test that attributes are initialized correctly
        self.assertEqual(self.review.place_id, '')
        self.assertEqual(self.review.user_id, '')
        self.assertEqual(self.review.text, '')

    def test_docstrings(self):
        # Check if class docstring and attributes docstrings are present
        self.assertIsNotNone(Review.__doc__)
        self.assertIsNotNone(Review.place_id.__doc__)
        self.assertIsNotNone(Review.user_id.__doc__)
        self.assertIsNotNone(Review.text.__doc__)

    def test_pep8_conformance(self):
        style = pycodestyle.StyleGuide(quiet=False)
        result = style.check_files([self.file_path])
        self.assertEqual(result.total_errors, 0, "PEP8 style violations found")

if __name__ == '__main__':
    unittest.main()