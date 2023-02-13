#!/usr/bin/pytnon3
import unittest
from models.base_model import BaseModel
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    def setUp(self):
        self.amenity = Amenity()

    def test_amenity_inheritance(self):
        self.assertTrue(issubclass(type(self.amenity), BaseModel))

    def test_attribute_types(self):
        self.assertIsInstance(self.amenity.name, str)

    def test_attribute_default_values(self):
        self.assertEqual(self.amenity.name, '')

    def test_assigning_valid_attribute_values(self):
        self.amenity.name = 'WiFi'
        self.assertEqual(self.amenity.name, 'WiFi')


if __name__ == '__main__':
    unittest.main()
