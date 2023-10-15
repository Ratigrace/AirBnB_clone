#!/usr/bin/python3
"""BaseModel test"""
import unittest
from models.base_model import BaseModel
import os
import pycodestyle
import uuid


class TestBaseModel(unittest.TestCase):
    """Test cases for the BaseModel"""

    def setUp(self) -> None:
        """Setups the class for the test"""

        self.base_model = BaseModel()
        self.base_file = "models/base_model.py"

    def tearDown(self) -> None:
        """Clean up the test generated resources"""

        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_init(self):
        """Test that 'id' is a UUID string"""

        self.assertTrue(isinstance(self.base_model.id, str))
        self.assertTrue(uuid.UUID(self.base_model.id, version=4))
        self.assertIsNotNone(self.base_model.created_at)
        self.assertIsNotNone(self.base_model.updated_at)

    def test_str(self):
        """Check if the __str__ method returns the expected string format"""

        expected_str = f"[{self.base_model.__class__.__name__}] \
({self.base_model.id}) {self.base_model.__dict__}"
        self.assertEqual(str(self.base_model), expected_str)

    def test_save(self):
        """Save the current updated_at time, then modify and save again"""

        original_updated_at = self.base_model.updated_at
        self.base_model.save()
        new_updated_at = self.base_model.updated_at
        self.assertGreater(new_updated_at, original_updated_at)

    def test_to_dict(self):
        """Test the to_dict method"""

        obj_dict = self.base_model.to_dict()
        self.assertEqual(obj_dict['__class__'],
                         self.base_model.__class__.__name__)
        self.assertEqual(obj_dict['created_at'],
                         self.base_model.created_at.isoformat())
        self.assertEqual(obj_dict['updated_at'],
                         self.base_model.updated_at.isoformat())

    def test_docstrings(self):
        """Check if class and method docstrings are present"""

        self.assertIsNotNone(BaseModel.__doc__)
        self.assertIsNotNone(BaseModel.__init__.__doc__)
        self.assertIsNotNone(BaseModel.__str__.__doc__)
        self.assertIsNotNone(BaseModel.save.__doc__)
        self.assertIsNotNone(BaseModel.to_dict.__doc__)

    def test_pep8_conformance(self):
        """Test for pep8 conformance"""
        
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files([self.base_file])
        self.assertEqual(result.total_errors, 0, "PEP8 style violations found")


if __name__ == "__main__":
    unittest.main()
