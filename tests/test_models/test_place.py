#!/usr/bin/python3
"""Class Place tests"""
import unittest
from datetime import datetime

from models.base_model import BaseModel
from models.place import Place


class Test_Place(unittest.TestCase):
    """Place class testing"""

    model = Place()

    def test_instance(self):
        """Test Is Instance"""
        self.assertIsInstance(self.model, BaseModel)
        self.assertIsInstance(self.model, Place)
        self.assertIsInstance(self.model.id, str)
        self.assertIsInstance(self.model.created_at, datetime)
        self.assertIsInstance(self.model.updated_at, datetime)

    def test_attributes(self):
        """Testing has attribute"""
        self.assertTrue(hasattr(self.model, "id"))
        self.assertTrue(hasattr(self.model, "created_at"))
        self.assertTrue(hasattr(self.model, "updated_at"))
        self.assertTrue(hasattr(self.model, "__init__"))
        self.assertTrue(hasattr(self.model, "city_id"))
        self.assertTrue(hasattr(self.model, "user_id"))
        self.assertTrue(hasattr(self.model, "name"))
        self.assertTrue(hasattr(self.model, "description"))
        self.assertTrue(hasattr(self.model, "number_rooms"))
        self.assertTrue(hasattr(self.model, "number_bathrooms"))
        self.assertTrue(hasattr(self.model, "max_guest"))
        self.assertTrue(hasattr(self.model, "price_by_night"))
        self.assertTrue(hasattr(self.model, "latitude"))
        self.assertTrue(hasattr(self.model, "longitude"))
        self.assertTrue(hasattr(self.model, "amenity_ids"))

    def test_attribute_type(self):
        """Testing Type of attr"""
        self.assertIsInstance(self.model.city_id, str)
        self.assertIsInstance(self.model.user_id, str)
        self.assertIsInstance(self.model.name, str)
        self.assertIsInstance(self.model.description, str)
        self.assertIsInstance(self.model.number_rooms, int)
        self.assertIsInstance(self.model.number_bathrooms, int)
        self.assertIsInstance(self.model.max_guest, int)
        self.assertIsInstance(self.model.price_by_night, int)
        self.assertIsInstance(self.model.latitude, float)
        self.assertIsInstance(self.model.longitude, float)
        self.assertIsInstance(self.model.amenity_ids, list)

    def test_add_attribute(self):
        """Testing add attribute"""
        self.model.rating = "4.5"
        self.assertTrue(hasattr(self.model, "rating"))


if __name__ == "__main__":
    unittest.main()
