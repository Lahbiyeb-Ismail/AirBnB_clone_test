#!/usr/bin/python3
"""Class Amenity tests"""
import unittest
from datetime import datetime

from models.amenity import Amenity
from models.base_model import BaseModel


class Test_Amenity(unittest.TestCase):
    """Amenity class testing"""

    model = Amenity()

    def test_instance(self):
        """Test Is Instance"""
        self.assertIsInstance(self.model, BaseModel)
        self.assertIsInstance(self.model, Amenity)
        self.assertIsInstance(self.model.id, str)
        self.assertIsInstance(self.model.created_at, datetime)
        self.assertIsInstance(self.model.updated_at, datetime)

    def test_attributes(self):
        """Testing has attribute"""
        self.assertTrue(hasattr(self.model, "id"))
        self.assertTrue(hasattr(self.model, "created_at"))
        self.assertTrue(hasattr(self.model, "updated_at"))
        self.assertTrue(hasattr(self.model, "__init__"))
        self.assertTrue(hasattr(self.model, "name"))

    def test_attribute_type(self):
        """Testing Type of attr"""
        self.assertIsInstance(self.model.name, str)

    def test_add_attribute(self):
        """Testing add attribute"""
        self.model.rating = "4.5"
        self.assertTrue(hasattr(self.model, "rating"))


if __name__ == "__main__":
    unittest.main()
