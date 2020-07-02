#!/usr/bin/python3
"""UNITTEST"""
import unittest
import os
from os import path
from models.city import City
from models.user import User
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class Test_FIle_Storage(unittest.TestCase):
    """ Test class file storage """
    def test_permissions(self):
        """ Test for validate the permissions """
        r = os.access('models/engine/file_storage.py', os.R_OK)
        self.assertTrue(r)
        w = os.access('models/engine/file_storage.py', os.W_OK)
        self.assertTrue(w)
        e = os.access('models/engine/file_storage.py', os.X_OK)
        self.assertTrue(e)