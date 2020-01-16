#! /usr/bin/env python3
import unittest
from employee import Employee


class test_empolyee(unittest.TestCase):
    def setUp(self):
        self.employee = Employee('Tony', 'Stark', 10000)

    def test_give_default_raise(self):
        self.employee.give_raise()
        self.assertEqual(self.employee.salary, 15000)

    def test_give_custom_raise(self):
        self.employee.give_raise(1000)
        self.assertEqual(self.employee.salary, 11000)


unittest.main()
