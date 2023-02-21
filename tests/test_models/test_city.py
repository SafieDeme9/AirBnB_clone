#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
from models.city import City


class TestCity(unittest.TestCase):

    def setUp(self):
        self.city = City()

    def test_city_inheritance(self):
        self.assertTrue(issubclass(type(self.city), BaseModel))

    def test_city_attributes(self):
        self.assertIsInstance(self.city, City)
        self.assertEqual(self.city.state_id, "")
        self.assertEqual(self.city.name, "")

    def test_city_attributes_values(self):
        self.city.state_id = "state_id_test"
        self.city.name = "name_test"
        self.assertEqual(self.city.state_id, "state_id_test")
        self.assertEqual(self.city.name, "name_test")


if __name__ == "__main__":
    unittest.main()
