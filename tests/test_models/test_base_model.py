#!/usr/bin/python3
import unittest
import models
from models.base_model import BaseModel


class Test_BaseModel(unittest.TestCase):
    """ Test class BaseModel """
    def setUp(self):
        self.model = BaseModel()

    def test_instantiation(self):
        """ """
        self.assertIsInstance(self.model, BaseModel)

    def test_atrributes(self):
        """ """
        self.assertTrue(hasattr(self.model, "created_at"))
        self.assertTrue(hasattr(self.model, "id"))
        self.assertTrue(hasattr(self.model, "updated_at"))
