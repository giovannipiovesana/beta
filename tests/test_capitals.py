#This module runs three different tests to the capitals.py module in both check_capital and check_state
import unittest
from directory.capitals import check_capital
from directory.capitals import check_state
import os
import sys

class TestTrue(unittest.TestCase):
    def setUp(self):
        self.list = str('Andorra')
        self.valid_state = 'Italy'
        self.list_boundary = ('andorra', 'aland island')
        self.list_empty = ()


#Test 1: test with an invalid type input.  
    def test_invalid (self):
        a = check_state(self.list)
        b = check_capital(self.list)
        self.assertFalse(a)
        self.assertFalse(b)
        
#test 2: Test with an empty list.
    def test_empty(self):
        c = check_state(self.list_empty)
        d = check_capital(self.list_empty)
        self.assertFalse(c)
        self.assertFalse(d)

#test 3: Test with a corner case since lowercase aren't allowed.
    def test_cornercase(self):
        e = check_state(self.list_boundary)
        f = check_capital(self.list_boundary)
        self.assertFalse(e)
        self.assertFalse(f)
 
    def tearDown(self):
        del self.list
        del self.list_empty
        del self.list_boundary
