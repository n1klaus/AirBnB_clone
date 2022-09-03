#!/usr/bin/env python3
""" Unittest test cases for 'models.base_model' """
import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel_Instantiation(unittest.TestCase):
    """Test the instantiation of the BaseModel class."""

    def setUp(self):
        self.model = BaseModel()

    def tearDown(self):
        del self.model

    def test_instance_exists(self):
        self.assertIsNotNone(self.model)

    def test_unique_ids(self):
        my_model = BaseModel()
        self.assertNotEqual(self.model.id, my_model.id)

    def test_creation_time(self):
        my_model = BaseModel()
        self.assertNotEqual(self.model.created_at, my_model.created_at)

    def test_no_args_instantiation(self):
        self.assertEqual(type(self.model), BaseModel)

    def test_instantiation(self):
        self.assertTrue(hasattr(self.model, 'id'))
        self.assertTrue(hasattr(self.model, 'created_at'))
        self.assertTrue(hasattr(self.model, 'updated_at'))

    def test_kwarg_instantiation(self):
        my_model = BaseModel(name="My First Model", number=89)
        self.assertTrue(hasattr(my_model, 'name'))
        self.assertTrue(hasattr(my_model, 'number'))

    def test_created_at_type(self):
        self.assertTrue(isinstance(self.model.created_at, datetime))

    def test_updated_at_type(self):
        self.assertTrue(isinstance(self.model.updated_at, datetime))

    def test_id_type(self):
        self.assertTrue(isinstance(self.model.id, str))


class TestBaseModel__str__(unittest.TestCase):
    """ Class to define test cases for public instance method '__str__()' """

    def setUp(self):
        self.model = BaseModel()

    def test_output_type(self):
        self.assertIsNotNone(self.model.__str__())
        self.assertIsInstance(self.model.__str__(), str)

    def test_contains_class_name(self):
        self.assertTrue(
                self.model.__str__().__contains__(
                    self.model.__class__.__name__
                    )
                )

    def test_contains_id(self):
        self.assertTrue(
                self.model.__str__().__contains__(self.model.id)
                )

    def test_contains__dict__(self):
        self.assertTrue(self.model.__str__().__contains__("id"))
        self.assertTrue(self.model.__str__().__contains__("created_at"))
        self.assertTrue(self.model.__str__().__contains__("updated_at"))

    def test_with_args(self):
        with self.assertRaises(TypeError):
            self.model.__str__("id")


class TestBaseModel_Save(unittest.TestCase):
    """ Class to define test cases for public instance method 'save()' """

    def setUp(self):
        self.model = BaseModel()

    def test_output_type(self):
        self.assertIsNone(self.model.save())

    def test_updated_at_type(self):
        self.assertIsInstance(self.model.updated_at, datetime)

    def test_update_time(self):
        updated_time = self.model.updated_at
        self.model.save()
        self.assertGreater(self.model.updated_at, updated_time)

    def test_with_args(self):
        with self.assertRaises(TypeError):
            self.model.save("id")


class TestBaseModel_to_dict(unittest.TestCase):
    """Test the `to_dict` instance method of the BaseModel class."""

    def setUp(self):
        self.model = BaseModel(name="My First Model", number=89)

    def test_to_dict(self):
        model_json = self.model.to_dict()
        self.assertDictEqual(model_json, {
            'id': self.model.id,
            'created_at': self.model.created_at.strftime(
                '%Y-%m-%dT%H:%M:%S.%f'),
            'updated_at': self.model.updated_at.strftime(
                '%Y-%m-%dT%H:%M:%S.%f'),
            'name': self.model.name,
            'number': self.model.number,
            '__class__': BaseModel.__name__})

    def test_to_dict_type(self):
        self.assertEqual(dict, type(self.model.to_dict()))

    def test_date_format(self):
        self.assertEqual(str, type(self.model.to_dict()['created_at']))
        self.assertEqual(str, type(self.model.to_dict()['updated_at']))

    def test_dict_value_types(self):
        model_json = self.model.to_dict()
        self.assertEqual(str, type(model_json['id']))
        self.assertEqual(str, type(model_json['name']))
        self.assertEqual(str, type(model_json['__class__']))
        self.assertEqual(int, type(model_json['number']))


if __name__ == '__main__':
    unittest.main()