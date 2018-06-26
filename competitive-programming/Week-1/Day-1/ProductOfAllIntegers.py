import unittest


def get_products_of_all_ints_except_at_index(list1):

    if len(list1) < 2:
        raise ValueError("Cannot find product of numbers of array length less than 2")
    
    #find the product of all integers before each index
    product = 1
    product_to_left = [1]*len(list1)
    for i in range(len(product_to_left)):
        product_to_left[i] = product
        product = product * list1[i]
        
    #find the product of all integers after each index
    product = 1
    product_to_right = [1]*len(list1)
    for j in range((len(product_to_right)-1),-1,-1):
        product_to_right[j] = product
        product = product * list1[j]
        
    #multiply the integers at same indices of product_to_left and product_to_right
    final_product = [1]*len(list1)
    for k in range(len(final_product)):
        final_product[k] = product_to_left[k]*product_to_right[k]

    return final_product
    
# Testcases

class Test(unittest.TestCase):

    def test_small_list(self):
        actual = get_products_of_all_ints_except_at_index([1, 2, 3])
        expected = [6, 3, 2]
        self.assertEqual(actual, expected)

    def test_longer_list(self):
        actual = get_products_of_all_ints_except_at_index([8, 2, 4, 3, 1, 5])
        expected = [120, 480, 240, 320, 960, 192]
        self.assertEqual(actual, expected)

    def test_list_has_one_zero(self):
        actual = get_products_of_all_ints_except_at_index([6, 2, 0, 3])
        expected = [0, 0, 36, 0]
        self.assertEqual(actual, expected)

    def test_list_has_two_zeros(self):
        actual = get_products_of_all_ints_except_at_index([4, 0, 9, 1, 0])
        expected = [0, 0, 0, 0, 0]
        self.assertEqual(actual, expected)

    def test_one_negative_number(self):
        actual = get_products_of_all_ints_except_at_index([-3, 8, 4])
        expected = [32, -12, -24]
        self.assertEqual(actual, expected)

    def test_all_negative_numbers(self):
        actual = get_products_of_all_ints_except_at_index([-7, -1, -4, -2])
        expected = [-8, -56, -14, -28]
        self.assertEqual(actual, expected)

    def test_error_with_empty_list(self):
        with self.assertRaises(Exception):
            get_products_of_all_ints_except_at_index([])

    def test_error_with_one_number(self):
        with self.assertRaises(Exception):
            get_products_of_all_ints_except_at_index([1])


unittest.main(verbosity=2)
