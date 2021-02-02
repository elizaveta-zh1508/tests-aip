import unittest
import random
import string
import task1


class ListTest(unittest.TestCase):
    def test_list_of_words(self):
        cases = [
            ([["black", "cat"], ["yellow", "mouse", "sun"], ["brown", "bear", "dog"]],
             ["yellow", "black", "brown", "mouse", "bear", "cat", "dog", "sun"]),
            ([["flower", "red", "pink"], ["tree", "leaves", "roots", "branch"]],
             ['branch', 'flower', 'leaves', 'roots', 'pink', 'tree', 'red']),
            ([["птица", "олень", "динозавр", "осень"], ["год", "месяц", "день"], ["зима", "весна", "лето", "осень"]],
             ['динозавр', 'весна', 'месяц', 'олень', 'осень', 'осень', 'птица', 'день', 'зима', 'лето', 'год'])
        ]
        for i, (two_dim, one_dim) in enumerate(cases):
            with self.subTest(case=i, two_dim=two_dim, one_dim=one_dim):
                self.assertEqual(one_dim, task1.list_of_words(two_dim))
