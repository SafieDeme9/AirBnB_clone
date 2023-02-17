#!/usr/bin/python3
""" FileStorage test driven"""
import os
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """ """
    def setUp(self):
        """ method creates an instance of the FileStorage class
            before each test is run
        """
        self.storage = FileStorage()

    def tearDown(self):
        """ method removes the file.json file after each test is run """
        try:
            os.remove("file.json")
        except Exception as excpt:
            pass

    def test_all(self):
        """ verifies that the all method returns a dictionary object """
        self.assertIsInstance(self.storage.all(), dict)

    def test_new(self):
        """ checks if the new method adds an object
            to the __objects dictionary
        """
        obj = BaseModel()
        self.storage.new(obj)
        self.assertIn(f"{obj.__class__.__name__}.{obj.id}",
                      self.storage.all().keys())

    def test_save(self):
        """ checks if the save method creates a file.json file """
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()
        self.assertTrue(os.path.isfile("file.json"))

    def test_reload(self):
        """ checks if the reload method loads the file.json file
            into the __objects dictionary
        """
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()
        self.storage.reload()
        self.assertIn(f"{obj.__class__.__name__}.{obj.id}",
                      self.storage.all().keys())


if __name__ == '__main__':
    unittest.main()
