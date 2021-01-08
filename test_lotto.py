import unittest
from lotto import *

#Class for implementing unit testing
class TestLottoTestCase(unittest.TestCase):
    lt = Lotto()
    
    #unit testing specific function
    def test_calc(self):
        assert lt.calc() == True, "Must return True"