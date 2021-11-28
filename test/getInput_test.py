import unittest
from utils.getInput import getInput

class GetInput_Tests(unittest.TestCase):
    def test_withTestId_ShoudlReturnCorrectly(self):
        self.assertEqual(getInput('test'), 'THIS IS A TEST FILE')
