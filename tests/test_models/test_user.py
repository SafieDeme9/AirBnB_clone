import unittest
import models
from models.base_model import BaseModel
from models.user import User
import os


class TestUserClass(unittest.TestCase):
    def setUp(self):
        self.user = User()

    def test_user_inheritance(self):
        self.assertTrue(issubclass(type(self.user), BaseModel))

    def test_user_attributes(self):
        self.assertEqual(self.user.email, '')
        self.assertEqual(self.user.password, '')
        self.assertEqual(self.user.first_name, '')
        self.assertEqual(self.user.last_name, '')

    def test_user_created_at(self):
        self.assertIsNotNone(self.user.created_at)

    def test_user_updated_at(self):
        self.assertIsNotNone(self.user.updated_at)

    def test_user_str_representation(self):
        expected_output = "[User] ({}) {}".format(self.user.id, self.user.__dict__)
        self.assertEqual(str(self.user), expected_output)


if __name__ == '__main__':
    unittest.main()
