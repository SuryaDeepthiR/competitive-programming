def get_max_profit(stocks):

    if len(stocks) < 2:
        raise ValueError('At least 2 prices is required, cannot trade at the same time')

    #update the first price and set the initial max_profit
    lowest_price  = stocks[0]
    max_profit = stocks[1] - stocks[0]

    for time in xrange(1, len(stocks)):
        #get the price at respective time(index)
        price = stocks[time]
        
        #update the profit selling at that price by buying at lowest_price
        profit = price - lowest_price
        
        #update the max_profit value and lowest_price
        max_profit = max(max_profit, profit)
        lowest_price = min(lowest_price, price)

    return max_profit

# Testcases

import unittest

class Test(unittest.TestCase):

    def test_price_goes_up_then_down(self):
        actual = get_max_profit([1, 5, 3, 2])
        expected = 4
        self.assertEqual(actual, expected)

    def test_price_goes_down_then_up(self):
        actual = get_max_profit([7, 2, 8, 9])
        expected = 7
        self.assertEqual(actual, expected)

    def test_price_goes_up_all_day(self):
        actual = get_max_profit([1, 6, 7, 9])
        expected = 8
        self.assertEqual(actual, expected)

    def test_price_goes_down_all_day(self):
        actual = get_max_profit([9, 7, 4, 1])
        expected = -2
        self.assertEqual(actual, expected)

    def test_price_stays_the_same_all_day(self):
        actual = get_max_profit([1, 1, 1, 1])
        expected = 0
        self.assertEqual(actual, expected)

    def test_one_price_raises_error(self):
        with self.assertRaises(Exception):
            get_max_profit([1])

    def test_empty_list_raises_error(self):
        with self.assertRaises(Exception):
            get_max_profit([])

unittest.main(verbosity=2)
