"""Homework 9.1 Test Cases."""


import unittest
import homeworks


class TestPerimeteryFunction(unittest.TestCase):
    def test_perimetery_negative_num(self):
        result = homeworks.perimetery(-3, -6, -7, -5)
        self.assertEqual(
            result,
            expected_result,
            msg=f'Test failed. Result {result} is not equal to ER'
        )
    
    def test_perimetery_zero_nums(self):
        pass


expected_result = -21
    

if __name__ == '__main__':
    unittest.main(verbosity=1)
