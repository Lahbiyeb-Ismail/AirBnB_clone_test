#!/usr/bin/python3
"""Class Review tests"""
import unittest
from datetime import datetime

from models.base_model import BaseModel
from models.review import Review


class Test_Review(unittest.TestCase):
    """Review class testing"""

    model = Review()

    def test_instance(self):
        """Test Is Instance"""
        self.assertIsInstance(self.model, BaseModel)
        self.assertIsInstance(self.model, Review)
        self.assertIsInstance(self.model.id, str)
        self.assertIsInstance(self.model.created_at, datetime)
        self.assertIsInstance(self.model.updated_at, datetime)

    def test_attributes(self):
        """Testing has attribute"""
        self.assertTrue(hasattr(self.model, "id"))
        self.assertTrue(hasattr(self.model, "created_at"))
        self.assertTrue(hasattr(self.model, "updated_at"))
        self.assertTrue(hasattr(self.model, "__init__"))
        self.assertTrue(hasattr(self.model, "place_id"))
        self.assertTrue(hasattr(self.model, "user_id"))
        self.assertTrue(hasattr(self.model, "text"))

    def test_attribute_type(self):
        """Testing Type of attr"""
        self.assertIsInstance(self.model.place_id, str)
        self.assertIsInstance(self.model.user_id, str)
        self.assertIsInstance(self.model.text, str)

    def test_add_attribute(self):
        """Testing add attribute"""
        self.model.rating = "4.5"
        self.assertTrue(hasattr(self.model, "rating"))


if __name__ == "__main__":
    unittest.main()
