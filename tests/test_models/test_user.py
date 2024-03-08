#!/usr/bin/python3
"""Class User tests"""
import unittest
from datetime import datetime

from models.base_model import BaseModel
from models.user import User


class Test_User(unittest.TestCase):
    """User class testing"""

    model = User()

    def test_instance(self):
        """Test Is Instance"""
        self.assertIsInstance(self.model, BaseModel)
        self.assertIsInstance(self.model, User)
        self.assertIsInstance(self.model.id, str)
        self.assertIsInstance(self.model.created_at, datetime)
        self.assertIsInstance(self.model.updated_at, datetime)

    def test_attributes(self):
        """Testing has attribute"""
        self.assertTrue(hasattr(self.model, "id"))
        self.assertTrue(hasattr(self.model, "created_at"))
        self.assertTrue(hasattr(self.model, "updated_at"))
        self.assertTrue(hasattr(self.model, "__init__"))
        self.assertTrue(hasattr(self.model, "email"))
        self.assertTrue(hasattr(self.model, "password"))
        self.assertTrue(hasattr(self.model, "first_name"))
        self.assertTrue(hasattr(self.model, "last_name"))

    def test_attribute_type(self):
        """Testing Type of attr"""
        self.assertIsInstance(self.model.email, str)
        self.assertIsInstance(self.model.password, str)
        self.assertIsInstance(self.model.first_name, str)
        self.assertIsInstance(self.model.last_name, str)

    def test_add_attribute(self):
        """Testing add attribute"""
        self.model.address = "address"
        self.assertTrue(hasattr(self.model, "address"))


if __name__ == "__main__":
    unittest.main()
