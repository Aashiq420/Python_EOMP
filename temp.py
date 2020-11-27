import unittest
from lotto import *

class TestLottoTestCase(unittest.TestCase):
    def test_calc(self):
        lt = Lotto()
        assert lt.calc() == True, "Must return True"