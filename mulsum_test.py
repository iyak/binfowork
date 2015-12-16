#!/usr/bin/env python

import unittest
import mulsum

class MulSumTest(unittest.TestCase):
    def test_add(self):
        self.assertEqual(mulsum.add(1,2), 3)
        self.assertEqual(mulsum.add(3,4), 7)
        self.assertEqual(mulsum.add(5,6), 11)
        self.assertEqual(mulsum.add(7,8), 15)
    def test_mult(self):
        self.assertEqual(mulsum.mult(1,2), 2)
        self.assertEqual(mulsum.mult(3,4), 12)
        self.assertEqual(mulsum.mult(5,6), 30)
        self.assertEqual(mulsum.add(7,8), 56)

if __name__ == '__main__':
    unittest.main()
