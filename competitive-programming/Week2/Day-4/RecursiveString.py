import unittest


def get_permutations(string):
    words = []
    stringRecursion(string,"",words)
    return set(words)

def stringRecursion(string, f, words):
    if len(string)==0:
        words.append(f)
        return
    for k in range(len(string)):
        stringRecursion(string[0:k]+string[k+1:],f+string[k],words)


# Tests

class Test(unittest.TestCase):

    def test_empty_string(self):
        actual = get_permutations('')
        expected = set([''])
        self.assertEqual(actual, expected)

    def test_one_character_string(self):
        actual = get_permutations('a')
        expected = set(['a'])
        self.assertEqual(actual, expected)

    def test_two_character_string(self):
        actual = get_permutations('ab')
        expected = set(['ab', 'ba'])
        self.assertEqual(actual, expected)

    def test_three_character_string(self):
        actual = get_permutations('abc')
        expected = set(['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)
