#!/usr/bin/python3
"""The Place model test case"""
import unittest
from models.place import Place
import pycodestyle

class TestPlace(unittest.TestCase):
    def setUp(self):
        self.place = Place()
        self.file_path = "models/place.py"

    def test_init(self):
        # Test that attributes are initialized correctly
        self.assertEqual(self.place.city_id, '')
        self.assertEqual(self.place.user_id, '')
        self.assertEqual(self.place.name, '')
        self.assertEqual(self.place.description, '')
        self.assertEqual(self.place.number_rooms, 0)
        self.assertEqual(self.place.number_bathrooms, 0)
        self.assertEqual(self.place.max_guest, 0)
        self.assertEqual(self.place.price_by_night, 0)
        self.assertEqual(self.place.latitude, 0.0)
        self.assertEqual(self.place.longitude, 0.0)
        self.assertEqual(self.place.amenity_ids, [])

    def test_docstrings(self):
        # Check if class docstring and attributes docstrings are present
        self.assertIsNotNone(Place.__doc__)
        self.assertIsNotNone(Place.city_id.__doc__)
        self.assertIsNotNone(Place.user_id.__doc__)
        self.assertIsNotNone(Place.name.__doc__)
        self.assertIsNotNone(Place.description.__doc__)
        self.assertIsNotNone(Place.number_rooms.__doc__)
        self.assertIsNotNone(Place.number_bathrooms.__doc__)
        self.assertIsNotNone(Place.max_guest.__doc__)
        self.assertIsNotNone(Place.price_by_night.__doc__)
        self.assertIsNotNone(Place.latitude.__doc__)
        self.assertIsNotNone(Place.longitude.__doc__)
        self.assertIsNotNone(Place.amenity_ids.__doc__)

    def test_pep8_conformance(self):
        style = pycodestyle.StyleGuide(quiet=False)
        result = style.check_files([self.file_path])
        self.assertEqual(result.total_errors, 0, "PEP8 style violations found")

if __name__ == '__main__':
    unittest.main()