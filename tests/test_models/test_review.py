#!/bin/usr/python3
import unittest
from models.base_model import BaseModel
from models.review import Review


class TestReview(unittest.TestCase):

    def setUp(self):
        self.review = Review()

    def test_review_inheritance(self):
        self.assertTrue(issubclass(type(self.review), BaseModel))

    def test_attribute_place_id(self):
        self.assertEqual(self.review.place_id, "")

    def test_attribute_user_id(self):
        self.assertEqual(self.review.user_id, "")

    def test_attribute_text(self):
        self.assertEqual(self.review.text, "")

    def test_attribute_created_at(self):
        self.assertIsNotNone(self.review.created_at)

    def test_attribute_updated_at(self):
        self.assertIsNotNone(self.review.updated_at)


if __name__ == '__main__':
    unittest.main()
