import unittest


def is_single_riffle(half1, half2, shuffled_deck):
    
    lh1 = len(half1)
    lh2 = len(half2)
    l = len(shuffled_deck)
    h1_i = 0
    h2_i = 0

    if lh1 + lh2 != l:
        return False

    for i in shuffled_deck:
        if h1_i<lh1 and i==half1[h1_i]:
            h1_i += 1
        elif h2_i<lh2 and i==half2[h2_i]:
            h2_i += 1
        elif i!=half1[h1_i] or i!=half2[h2_i]:
            return False 
    return True





# Tests

class Test(unittest.TestCase):

    def test_both_halves_are_the_same_length(self):
        result = is_single_riffle([1, 4, 5], [2, 3, 6], [1, 2, 3, 4, 5, 6])
        self.assertTrue(result)

    def test_halves_are_different_lengths(self):
        result = is_single_riffle([1, 5], [2, 3, 6], [1, 2, 6, 3, 5])
        self.assertFalse(result)

    def test_one_half_is_empty(self):
        result = is_single_riffle([], [2, 3, 6], [2, 3, 6])
        self.assertTrue(result)

    def test_shuffled_deck_is_missing_cards(self):
        result = is_single_riffle([1, 5], [2, 3, 6], [1, 6, 3, 5])
        self.assertFalse(result)

    def test_shuffled_deck_has_extra_cards(self):
        result = is_single_riffle([1, 5], [2, 3, 6], [1, 2, 3, 5, 6, 8])
        self.assertFalse(result)


unittest.main(verbosity=2)
