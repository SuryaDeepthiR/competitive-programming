import unittest
def Get_binary(x):
    num = ""
    if x is 0: return "0"
    while(x!=0):
        temp = x%2
        x = x//2
        num = num + str(temp)
    return num

def Hamming_distance(x,y):
    bx = Get_binary(x)
    by = Get_binary(y)
    count = 0
    if len(bx) > len(by): 
        for i in xrange(len(by),len(bx)):
            by = by + "0"
    if len(by) > len(bx):
        for i in xrange(len(bx),len(by)):
            bx = bx + "0"
    for i in xrange(0,len(bx)):
        if bx[i] != by[i]:
            count = count + 1
        else:
            pass
    return count

# Tests

class Test(unittest.TestCase):

    def testcase1(self):
        x = 25
        y = 30
        actual = Hamming_distance(x,y)
        expected = 3
        self.assertEqual(actual, expected)

    def testcase2(self):
        x = 1 
        y = 4
        actual = Hamming_distance(x,y)
        expected = 2
        self.assertEqual(actual, expected)

    def testcase3(self):
        x = 100 
        y = 250
        actual = Hamming_distance(x,y)
        expected = 5
        self.assertEqual(actual, expected)

    def testcase4(self):
        x = 1
        y = 30
        actual = Hamming_distance(x,y)
        expected = 5
        self.assertEqual(actual, expected)

    def testcase5(self):
        x = 0
        y = 255
        actual = Hamming_distance(x,y)
        expected = 8
        self.assertEqual(actual, expected)

    Hamming_distance(0,255)

unittest.main(verbosity=2)
