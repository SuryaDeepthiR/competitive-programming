import unittest


def has_palindrome_permutation(the_string):

    # Check if any permutation of the input is a palindrome
    
    dic = {}
    
    for i in range(0,len(the_string)):
        
        if the_string[i] not in dic:
            dic[the_string[i]] = 1
        else:
            dic[the_string[i]] += 1
    
    count = 0
    
    for key in dic:
        if (dic[key] == 1):
            count += 1
    
    if count > 1:
        return False
    
    return True


# Tests
class Test(unittest.TestCase):

    def test_permutation_with_odd_number_of_chars(self):
        result = has_palindrome_permutation('aabcbcd')
        self.assertTrue(result)

    def test_permutation_with_even_number_of_chars(self):
        result = has_palindrome_permutation('aabccbdd')
        self.assertTrue(result)

    def test_no_permutation_with_odd_number_of_chars(self):
        result = has_palindrome_permutation('aabcd')
        self.assertFalse(result)

    def test_no_permutation_with_even_number_of_chars(self):
        result = has_palindrome_permutation('aabbcd')
        self.assertFalse(result)

    def test_empty_string(self):
        result = has_palindrome_permutation('')
        self.assertTrue(result)

    def test_one_character_string(self):
        result = has_palindrome_permutation('a')
        self.assertTrue(result)


unittest.main(verbosity=2)
