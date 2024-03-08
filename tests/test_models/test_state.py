#!/usr/bin/python3
"""Class State tests"""
import unittest
from datetime import datetime

from models.base_model import BaseModel
from models.state import State


class Test_State(unittest.TestCase):
    """Class State testing"""

    model = State()

    def test_instance(self):
        """Test Is Instance"""
        self.assertIsInstance(self.model, BaseModel)
        self.assertIsInstance(self.model, State)
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
        self.model.some = "some"
        self.assertTrue(hasattr(self.model, "some"))


if __name__ == "__main__":
    unittest.main()
