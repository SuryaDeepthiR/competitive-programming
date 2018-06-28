import unittest

class Trie(object):

    # Implement a trie and use it to efficiently store strings
    
    def __init__(self):
        self.dict = {}
        self.valid = False

    def add_word(self, word):
        if len(word) == 0:
            node = Trie()
            if word in self.dict:
                return False
            else:
                node = Trie()
                node.valid = True
                self.dict[word] = node
                return True
        root = word[0]
        if root in self.dict:
            node = self.dict[root]
        else:
            node = Trie()
            self.dict[root] = node

        if len(word) > 1:
            remains = word[1:]
            return node.add_word(remains)
        else:
            if node.valid:
                return False
            else:
                self.dict[root].valid = True
                return True  

# Tests

class Test(unittest.TestCase):

    def test_trie_usage(self):
        trie = Trie()

        result = trie.add_word('catch')
        self.assertTrue(result, msg='new word 1')

        result = trie.add_word('cakes')
        self.assertTrue(result, msg='new word 2')

        result = trie.add_word('cake')
        self.assertTrue(result, msg='prefix of existing word')

        result = trie.add_word('cake')
        self.assertFalse(result, msg='word already present')

        result = trie.add_word('caked')
        self.assertTrue(result, msg='new word 3')

        result = trie.add_word('catch')
        self.assertFalse(result, msg='all words still present')

        result = trie.add_word('')
        self.assertTrue(result, msg='empty word')

        result = trie.add_word('')
        self.assertFalse(result, msg='empty word present')


unittest.main(verbosity=2)
