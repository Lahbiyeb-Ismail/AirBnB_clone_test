#!/usr/bin/python3

import unittest
from datetime import datetime

from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Test BaseModel class"""

    def setUp(self):
        self.base_model = BaseModel()

    def test_init(self):
        self.assertIsInstance(self.base_model.id, str)
        self.assertIsInstance(self.base_model.created_at, datetime)
        self.assertIsInstance(self.base_model.updated_at, datetime)

    def test_attributes(self):
        self.assertTrue(hasattr(self.base_model, "id"))
        self.assertTrue(hasattr(self.base_model, "created_at"))
        self.assertTrue(hasattr(self.base_model, "updated_at"))

    def test_id_is_generated_on_init(self):
        model = BaseModel()
        self.assertIsNotNone(model.id)
        self.assertIsInstance(model.id, str)

    def test_created_at_is_set_on_init(self):
        model = BaseModel()
        self.assertIsNotNone(model.created_at)
        self.assertIsInstance(model.created_at, datetime)

    def test_updated_at_is_set_on_init(self):
        model = BaseModel()
        self.assertIsNotNone(model.updated_at)
        self.assertIsInstance(model.updated_at, datetime)

    # def test_created_at_equals_updated_at_on_init(self):
    #     model = BaseModel()
    #     self.assertEqual(model.created_at, model.updated_at)

    def test_two_models_have_different_ids(self):
        model1 = BaseModel()
        model2 = BaseModel()
        self.assertNotEqual(model1.id, model2.id)

    def test_str_representation(self):
        model = BaseModel()
        expected = "[{}] ({}) {}".format(
            model.__class__.__name__, model.id, model.__dict__
        )
        self.assertEqual(str(model), expected)

    def test_save_updates_updated_at(self):
        model = BaseModel()
        old_updated_at = model.updated_at
        model.save()
        self.assertNotEqual(old_updated_at, model.updated_at)

    def test_to_dict_contains_correct_keys(self):
        model = BaseModel()
        model_dict = model.to_dict()
        expected_keys = ["__class__", "id", "created_at", "updated_at"]
        self.assertCountEqual(model_dict.keys(), expected_keys)

    def test_to_dict_contains_added_attributes(self):
        model = BaseModel()
        model.name = "My Model"
        model_dict = model.to_dict()
        self.assertEqual(model_dict["name"], "My Model")


if __name__ == "__main__":
    unittest.main()
