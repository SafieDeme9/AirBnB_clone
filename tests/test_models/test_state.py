#!/usr/bin/python3
import unittest
from models.state import State
from models.base_model import BaseModel


class TestState(unittest.TestCase):
    """ Creating a test class """
    def test_state_inherits_from_base_model(self):
        """ Checks if the State class inherits from the BaseModel class """
        state = State()
        self.assertTrue(isinstance(state, BaseModel))

    def test_state_has_name_attribute(self):
        """ Verifies that the State class has a name attribute """
        state = State()
        self.assertTrue(hasattr(state, 'name'))

    def test_name_attribute_is_empty_string_by_default(self):
        """ Checks that the name attribute is an empty string by default """
        state = State()
        self.assertEqual(state.name, '')

    def test_name_attribute_can_be_set(self):
        """ Checks if the name attribute can be set to a new value """
        state = State()
        state.name = 'California'
        self.assertEqual(state.name, 'California')


if __name__ == '__main__':
    unittest.main()
