import unittest
from models.base_model import BaseModel
from models.place import Place


class TestPlace(unittest.TestCase):

    def setUp(self):
        self.place = Place()

    def test_place_inheritance(self):
        self.assertIsInstance(self.place, BaseModel)

    def test_place_has_attribute_city_id(self):
        self.assertTrue(hasattr(self.place, "city_id"))

    def test_place_has_attribute_user_id(self):
        self.assertTrue(hasattr(self.place, "user_id"))

    def test_place_has_attribute_name(self):
        self.assertTrue(hasattr(self.place, "name"))

    def test_place_has_attribute_description(self):
        self.assertTrue(hasattr(self.place, "description"))

    def test_place_has_attribute_number_rooms(self):
        self.assertTrue(hasattr(self.place, "number_rooms"))

    def test_place_has_attribute_number_bathrooms(self):
        self.assertTrue(hasattr(self.place, "number_bathrooms"))

    def test_place_has_attribute_max_guest(self):
        self.assertTrue(hasattr(self.place, "max_guest"))

    def test_place_has_attribute_price_by_night(self):
        self.assertTrue(hasattr(self.place, "price_by_night"))

    def test_place_has_attribute_latitude(self):
        self.assertTrue(hasattr(self.place, "latitude"))

    def test_place_has_attribute_longitude(self):
        self.assertTrue(hasattr(self.place, "longitude"))

    def test_place_has_attribute_amenity_ids(self):
        self.assertTrue(hasattr(self.place, "amenity_ids"))


if __name__ == '__main__':
    unittest.main()
