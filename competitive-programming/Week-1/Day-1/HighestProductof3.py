import unittest
import sys

maxi = sys.maxsize
mini = -sys.maxsize-1

def highest_product_of_3(array):
    if len(array) < 3:
        raise ValueError("Cannot find the highest product of 3 without 3 values")

    maximum1 = mini
    maximum2 = mini
    maximum3 = mini
    minimum1 = maxi
    minimum2 = maxi

    for i in range(0,len(array)):
        if array[i] > maximum1:
            maximum3 = maximum2
            maximum2 = maximum1
            maximum1 = array[i]

        elif array[i] > maximum2:
            maximum3 = maximum2
            maximum2 = array[i]

        elif array[i] > maximum3:
            maximum3 = array[i]

        if array[i] < minimum1:
            minimum2 = minimum1
            minimum1 = array[i] 

        elif array[i] < minimum2:
            minimum2 = array[i]

    return max((minimum1*minimum2*maximum1),(maximum1*maximum2*maximum3))



# Testcases

class Test(unittest.TestCase):

    def test_short_list(self):
        actual = highest_product_of_3([1, 2, 3, 4])
        expected = 24
        self.assertEqual(actual, expected)

    def test_longer_list(self):
        actual = highest_product_of_3([6, 1, 3, 5, 7, 8, 2])
        expected = 336
        self.assertEqual(actual, expected)

    def test_list_has_one_negative(self):
        actual = highest_product_of_3([-5, 4, 8, 2, 3])
        expected = 96
        self.assertEqual(actual, expected)

    def test_list_has_two_negatives(self):
        actual = highest_product_of_3([-10, 1, 3, 2, -10])
        expected = 300
        self.assertEqual(actual, expected)

    def test_list_is_all_negatives(self):
        actual = highest_product_of_3([-5, -1, -3, -2])
        expected = -6
        self.assertEqual(actual, expected)

    def test_error_with_empty_list(self):
        with self.assertRaises(Exception):
            highest_product_of_3([])

    def test_error_with_one_number(self):
        with self.assertRaises(Exception):
            highest_product_of_3([1])

    def test_error_with_two_numbers(self):
        with self.assertRaises(Exception):
            highest_product_of_3([1, 1])


unittest.main(verbosity=2)
