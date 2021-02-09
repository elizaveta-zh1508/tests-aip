import unittest
import kr02_02_2021


class ListTest(unittest.TestCase):
    def test_task_1(self):
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
                self.assertEqual(one_dim, kr02_02_2021.task_1(two_dim))

    def test_task_3(self):
        cases = [
            ("11354896115777", {7: 3, 1: 4, 5: 2}),
            ("11354896115777316689764163156879641631794631594", {7: 6, 1: 10, 6: 9}),
            ("000000000000", {0: 12}),
            ("001122334455", {3: 2, 1: 2, 2: 2, 4: 2, 5: 2, 0: 2})
        ]
        for i, (digits, dictionary) in enumerate(cases):
            with self.subTest(case=i, digits=digits, dictionary=dictionary):
                self.assertEqual(dictionary, kr02_02_2021.task_3(digits))

    def test_task_4_1(self):
        cases = [
            (("Alaska", "auto", "arc", "agenda", "arugula", "caveman"), (9, 4, 4, 4)),
            (("mammal", "mnemonic", "scam", "momentum", "memory", "mankind"), (4,))
        ]
        for i, (inp, outp) in enumerate(cases):
            with self.subTest(case=i, inp=inp, outp=outp):
                self.assertEqual(outp, kr02_02_2021.task_4_1(inp))

    def test_task_4_2(self):
        cases = [
            (("Alaska", "auto", "arc", "agenda", "arugula", "caveman"), {4, 6, 7}),
            (("mammal", "mnemonic", "scam", "momentum", "memory", "mankind"), {8, 4, 6, 7})
        ]
        for i, (inp, outp) in enumerate(cases):
            with self.subTest(case=i, inp=inp, outp=outp):
                self.assertEqual(outp, kr02_02_2021.task_4_2(inp))

    def test_task_4_3(self):
        cases = [
            (("Alaska", "auto", "arc", "agenda", "arugula", "caveman"), ['lsk', 'gnd', 'rgl']),
            (("mammal", "mnemonic", "scam", "momentum", "memory", "mankind"), [])
        ]
        for i, (inp, outp) in enumerate(cases):
            with self.subTest(case=i, inp=inp, outp=outp):
                self.assertEqual(outp, kr02_02_2021.task_4_3(inp))

    def test_task_5(self):
        cases = [
            ([1, 2, 4, 5, 5], [1, 3, 4], [2, 5]),
            ([15, 3, 4, 79, 63, 1], [1, 3, 4], [15, 63, 79]),
            ([0, 0, 0], [0, 0, 0], [])
        ]
        for i, (inp1, inp2, outp) in enumerate(cases):
            with self.subTest(case=i, inp1=inp1, inp2=inp2, outp=outp):
                self.assertEqual(outp, kr02_02_2021.task_5(inp1, inp2))

    def test_task_6(self):
        cases = [
            ([1, 2, 4, 5, 5], (5, 4, 2, 1)),
            ([1], (1,)),
            ([1, 3, 4, 15, 63, 79], (79, 63, 15, 4, 3, 1))
        ]
        for i, (inp, outp) in enumerate(cases):
            with self.subTest(case=i, inp=inp, outp=outp):
                self.assertEqual(outp, kr02_02_2021.task_6(inp))
