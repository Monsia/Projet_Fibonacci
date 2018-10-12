import unittest
from Fibonacci import *


class MyFirstTests(unittest.TestCase):

    def test_Fibonacci1(self):
        self.assertEqual(Fibonacci(5),5)

    def test_Fibonacci2(self):
        self.assertEqual(Fibonacci(6),8)
