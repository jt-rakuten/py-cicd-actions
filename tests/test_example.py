# tests/test_example.py

import unittest
from my_module.example import add

class TestExample(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(1, 2), 3)

if __name__ == '__main__':
    unittest.main()

