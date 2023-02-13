import unittest
from models.state import State


class TestState(unittest.TestCase):
    def test_state_attributes(self):
        state = State()
        self.assertEqual(state.name, '')

    def test_state_str_representation(self):
        state = State()
        state.name = 'California'
        self.assertEqual(str(state), '[State] (None) California')

    def test_state_to_dict_representation(self):
        state = State()
        state.name = 'California'
        expected_output = {
            'id': None,
            'created_at': None,
            'updated_at': None,
            'name': 'California'
        }
        self.assertDictEqual(state.to_dict(), expected_output)


if __name__ == '__main__':
    unittest.main()
