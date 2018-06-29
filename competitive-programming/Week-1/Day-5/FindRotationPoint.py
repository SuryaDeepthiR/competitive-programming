import unittest


def find_rotation_point(words):

    # Find the rotation point in the list
    first_word = words[0]
    lo = 0
    hi = len(words) - 1
    if words[lo]<words[hi]:
        return lo
    while lo <= hi:
        mid = lo + (hi-lo)//2
 
 
        if words[mid] < first_word: 
            hi = mid
        elif words[mid] > first_word:   
            lo = mid
    
        if lo+1 == hi:
            return hi



# Tests

class Test(unittest.TestCase):

    def test_small_list(self):
        actual = find_rotation_point(['cape', 'cake'])
        expected = 1
        self.assertEqual(actual, expected)

    def test_medium_list(self):
        actual = find_rotation_point(['grape', 'orange', 'plum',
                                      'radish', 'apple'])
        expected = 4
        self.assertEqual(actual, expected)

    def test_large_list(self):
        actual = find_rotation_point(['ptolemaic', 'retrograde', 'supplant',
                                      'undulate', 'xenoepist', 'asymptote',
                                      'babka', 'banoffee', 'engender',
                                      'karpatka', 'othellolagkage'])
        expected = 5
        self.assertEqual(actual, expected)
        

    # Are we missing any edge cases?


unittest.main(verbosity=2)
