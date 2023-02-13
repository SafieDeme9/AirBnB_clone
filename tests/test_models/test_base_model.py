#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
from datetime import datetime

"""
Test base model
"""


class TestBaseModel(unittest.TestCase):
    def test_isinstance(self):
        bm = BaseModel()
        self.assertIsInstance(bm, BaseModel)
        self.assertIsInstance(bm.id, str)
        self.assertIsInstance(bm.created_at, datetime)
        self.assertIsInstance(bm.updated_at, datetime)

    def test_init_with_kwargs(self):
        bm_dict = {
            'id': '12345678-1234-1234-1234-123456789012',
            'created_at': '2022-06-14T22:31:03.285259',
            'updated_at': '2022-06-15T22:31:03.285259',
            'foo': 'bar'
        }
        bm = BaseModel(**bm_dict)
        self.assertEqual(bm.id, bm_dict['id'])
        self.assertEqual(bm.created_at, datetime.
                         strptime(bm_dict['created_at'],
                                  '%Y-%m-%dT%H:%M:%S.%f'))
        self.assertEqual(bm.updated_at, datetime.
                         strptime(bm_dict['updated_at'],
                                  '%Y-%m-%dT%H:%M:%S.%f'))
        self.assertEqual(bm.foo, bm_dict['foo'])

    def test_save(self):
        bm = BaseModel()
        updated_at = bm.updated_at
        bm.save()
        self.assertEqual(updated_at, bm.updated_at)

    def test_to_dict(self):
        bm = BaseModel()
        d = bm.to_dict()
        self.assertIsInstance(d, dict)
        self.assertEqual(d["__class__"], "BaseModel")
        self.assertEqual(d["id"], bm.id)
        self.assertEqual(d["created_at"], bm.created_at.isoformat())
        self.assertEqual(d["updated_at"], bm.updated_at.isoformat())

# if __name__ == "__main__":
#    unittest.main()
