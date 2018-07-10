import unittest


def find_repeat(the_list):
    
    low = 1
    high = len(the_list) - 1

    while low < high:
        mid = low + ((high - low) // 2)
        ll, lh = low, mid
        ul, uh = mid+1, high

        ElementsInLowerRange = 0
        for element in the_list:
            if ll <= element <= lh:
                ElementsInLowerRange += 1

        distinctPossibleIntegers = (lh - ll + 1)
        
        if ElementsInLowerRange > distinctPossibleIntegers:
            low, high = ll, lh
        else:
            low, high = ul, uh

    return low


# Tests

class Test(unittest.TestCase):

    def test_just_the_repeated_number(self):
        actual = find_repeat([1, 1])
        expected = 1
        self.assertEqual(actual, expected)

    def test_short_list(self):
        actual = find_repeat([1, 2, 3, 2])
        expected = 2
        self.assertEqual(actual, expected)

    def test_medium_list(self):
        actual = find_repeat([1, 2, 5, 5, 5, 5])
        expected = 5
        self.assertEqual(actual, expected)

    def test_long_list(self):
        actual = find_repeat([4, 1, 4, 8, 3, 2, 7, 6, 5])
        expected = 4
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)
