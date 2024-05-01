import os
import pickle
import unittest
from dataclasses import dataclass
from main import Fexdb


class TestFexdb(unittest.TestCase):

    def setUp(self):
        self.db_filename = 'test_db.pkl'
        self.db = Fexdb(self.db_filename)

    def tearDown(self):
        if os.path.exists(self.db_filename):
            os.remove(self.db_filename)

    def test_add_and_get(self):
        test_key = 'test_key'
        test_value = {'field1': 'value1', 'field2': 'value2'}
        self.db.add(test_key, test_value)
        self.assertEqual(self.db.get(test_key), test_value)

    def test_delete(self):
        test_key = 'test_key'
        test_value = {'field1': 'value1', 'field2': 'value2'}
        self.db.add(test_key, test_value)
        self.db.delete(test_key)
        self.assertIsNone(self.db.get(test_key))

    def test_update(self):
        test_key = 'test_key'
        test_value1 = {'field1': 'value1', 'field2': 'value2'}
        test_value2 = {'field1': 'new_value1', 'field2': 'new_value2'}
        self.db.add(test_key, test_value1)
        self.db.update(test_key, test_value2)
        self.assertEqual(self.db.get(test_key), test_value2)

    def test_edge_cases(self):
        empty_key = ''
        empty_value = {}
        self.db.add(empty_key, empty_value)
        self.assertEqual(self.db.get(empty_key), empty_value)
        empty_key = ''
        empty_value = {}
        self.db.update(empty_key, empty_value)
        self.assertEqual(self.db.get(empty_key), empty_value)

if __name__ == '__main__':
    unittest.main()
