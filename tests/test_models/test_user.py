#!/src/bin/python3
import unittest
import models
import os
import sys
from datetime import datetime
from models.base_model import BaseModel
from models.user import User


class TestUser(unittest.TestCase):
    """ Test class User """
    def setUp(self):
        self.usr1 = User()
        test_user = {'id': '15069027-908d-4ea7-b9d7-235a379f1287',
                     'created_at': '2020-07-01T08:53:34.437226',
                     'updated_at': '2020-07-01T08:53:34.437437',
                     'name': 'Students',
                     'email': 'holbie@hbtn.co',
                     'password': "h01b3rt0n",
                     'first_name': "Betty",
                     'last_name': "Holberton"}
        self.usr2 = User(**test_user)
        self.usr2.save()

    def tearDown(self):
        """cleaning the file.json"""
        sys.stdout = sys.__stdout__
        os.remove("file.json")

    def test_instantiation(self):
        """ Test instantiation """
        self.assertIsInstance(self.usr1, User)

    def test_atrributes_noargs(self):
        """ Testing instantiation attributtes """
        self.assertTrue(hasattr(self.usr1, "created_at"))
        self.assertTrue(hasattr(self.usr1, "id"))
        self.assertTrue(hasattr(self.usr1, "updated_at"))
        self.assertTrue(hasattr(self.usr1, "email"))
        self.assertTrue(hasattr(self.usr1, "password"))
        self.assertTrue(hasattr(self.usr1, "first_name"))
        self.assertTrue(hasattr(self.usr1, "last_name"))

    def test_atrributes_kwargs(self):
        """ Testing instantiation attributtes """
        self.assertTrue(hasattr(self.usr2, "created_at"))
        self.assertTrue(hasattr(self.usr2, "id"))
        self.assertTrue(hasattr(self.usr2, "updated_at"))
        self.assertTrue(hasattr(self.usr2, "email"))
        self.assertEqual(self.usr2.email, 'holbie@hbtn.co')
        self.assertTrue(hasattr(self.usr2, "password"))
        self.assertEqual(self.usr2.password, 'h01b3rt0n')
        self.assertTrue(hasattr(self.usr2, "first_name"))
        self.assertEqual(self.usr2.first_name, 'Betty')
        self.assertTrue(hasattr(self.usr2, "last_name"))
        self.assertEqual(self.usr2.last_name, 'Holberton')

    def test_save(self):
        """ Testing save() function """
        created = self.usr1.created_at
        old = self.usr1.updated_at
        self.usr1.save()
        new = self.usr1.updated_at
        self.assertNotEqual(old, new)

    def test_to_dict_noargs(self):
        """ Testing to_dict() Function """
        jsonfile = self.usr1.to_dict()
        self.assertNotEqual(self.usr1.__dict__, jsonfile)
        self.assertNotIsInstance(jsonfile["created_at"], datetime)
        self.assertNotIsInstance(jsonfile["updated_at"], datetime)
        self.assertTrue(hasattr(jsonfile, "__class__"))
        self.assertEqual(jsonfile["__class__"], "User")

    def test_to_dict_kwargs(self):
        """ Testing to_dict() function, instantiation with kwargs"""
        jsonfile2 = self.usr2.to_dict()
        self.assertNotEqual(self.usr2.__dict__, jsonfile2)
        self.assertNotIsInstance(jsonfile2["created_at"], datetime)
        self.assertNotIsInstance(jsonfile2["updated_at"], datetime)
        self.assertEqual(jsonfile2["created_at"], '2020-07-01T08:53:34.437226')
        self.assertTrue(hasattr(jsonfile2, "__class__"))
        self.assertEqual(jsonfile2["__class__"], "User")

    def test_string(self):
        """Testing __str__() the correct output"""
        string = "[BaseModel] ({}) {}".format(self.usr1.id, self.usr1.__dict__)
        self.assertEqual(string, str(self.usr1))

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
