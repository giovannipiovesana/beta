'''This module runs three different tests to the capitals.py module in both
check_capital and check_state functions.'''
import unittest
from directory.capitals import check_capital
from directory.capitals import check_state
import os
import sys


class TestTrue(unittest.TestCase):

    def setUp(self):
        self.list = str('Andorra')
        self.list_boundary = ('andorra', 'aland island')
        self.list_empty = ()

    def test_invalid(self):
        ''' Test 1: test with an invalid type input.'''
        a = check_state(self.list)
        b = check_capital(self.list)
        self.assertFalse(a)
        self.assertFalse(b)

    def test_empty(self):
        ''' Test 2: Test with an empty list.'''
        c = check_state(self.list_empty)
        d = check_capital(self.list_empty)
        self.assertFalse(c)
        self.assertFalse(d)

    def test_cornercase(self):
        ''' Test 3: Test with a corner case since lowercase aren't allowed.'''
        e = check_state(self.list_boundary)
        f = check_capital(self.list_boundary)
        self.assertFalse(e)
        self.assertFalse(f)

    def tearDown(self):
        del self.list
        del self.list_empty
        del self.list_boundary
