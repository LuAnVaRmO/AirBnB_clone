#!/usr/bin/python3
import unittest
import models
import os
import sys
from datetime import datetime
from models.base_model import BaseModel


class Test_BaseModel(unittest.TestCase):
    """ Test class BaseModel """
    def setUp(self):
        self.obj1 = BaseModel()
        argv = {"id": "15069027-908d-4ea7-b9d7-235a379f1287",
                "created_at": "2020-07-01T08:53:34.437226",
                "updated_at": "2020-07-01T08:53:34.437437",
                "name": "Holberton"}
        self.obj2 = BaseModel(**argv)
        self.obj2.save()

    def tearDown(self):
        """cleaning the file.json"""
        sys.stdout = sys.__stdout__
        os.remove("file.json")

    def test_instantiation(self):
        """ Test instantiation """
        self.assertIsInstance(self.obj1, BaseModel)
        self.assertIsInstance(self.obj2, BaseModel)

    def test_atrributes_noargs(self):
        """ Testing instantiation attributtes """
        self.assertTrue(hasattr(self.obj1, "created_at"))
        self.assertTrue(hasattr(self.obj1, "id"))
        self.assertTrue(hasattr(self.obj1, "updated_at"))

    def test_attr_kwargs(self):
        """Testing instatiation with kwargs"""
        self.assertEqual(self.obj2.name, 'Holberton')
        self.assertEqual(self.obj2.id, '15069027-908d-4ea7-b9d7-235a379f1287')
        self.assertEqual(self.obj2.created_at,
                         datetime(2020, 7, 1, 8, 53, 34, 437226))

    def test_save(self):
        """ Testing save() function """
        created = self.obj1.created_at
        old = self.obj1.updated_at
        self.obj1.save()
        new = self.obj1.updated_at
        self.assertNotEqual(old, new)

    def test_to_dict_noargs(self):
        """ Testing to_dict() Function """
        jsonfile = self.obj1.to_dict()
        self.assertNotEqual(self.obj1.__dict__, jsonfile)
        self.assertNotIsInstance(jsonfile["created_at"], datetime)
        self.assertNotIsInstance(jsonfile["updated_at"], datetime)
        self.assertTrue(hasattr(jsonfile, "__class__"))
        self.assertEqual(jsonfile["__class__"], "BaseModel")

    def test_to_dict_kwargs(self):
        """ Testing to_dict() function, instantiation with kwargs"""
        jsonfile2 = self.obj2.to_dict()
        self.assertNotEqual(self.obj2.__dict__, jsonfile2)
        self.assertNotIsInstance(jsonfile2["created_at"], datetime)
        self.assertNotIsInstance(jsonfile2["updated_at"], datetime)
        self.assertEqual(jsonfile2["created_at"], '2020-07-01T08:53:34.437226')
        self.assertTrue(hasattr(jsonfile2, "__class__"))
        self.assertEqual(jsonfile2["__class__"], "BaseModel")

    def test_string(self):
        """Testing __str__() the correct output"""
        string = "[BaseModel] ({}) {}".format(self.obj1.id, self.obj1.__dict__)
        self.assertEqual(string, str(self.obj1))

    def test_permissions(self):
        """ Test for validate the permissions """
        r = os.access('models/user.py', os.R_OK)
        self.assertTrue(r)
        w = os.access('models/user.py', os.W_OK)
        self.assertTrue(w)
        e = os.access('models/user.py', os.X_OK)
        self.assertTrue(e)


if __name__ == "__main__":
    unittest.main()
