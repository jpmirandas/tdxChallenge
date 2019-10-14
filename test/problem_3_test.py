import unittest
from answers.problem_3 import Problem3


class TestProblem3(unittest.TestCase):

    def setUp(self):
        self.problem = Problem3()

        self.list_1 = [3, 5, 768, 3, 6, 23, 98, 38, 32, 45, 34, 234]
        self.list_2 = [10, 12, 43, 74, 25, 56, 37, 98, 29, 10]
        self.expected_result = 80

    def test_most_frequent_digit(self):
        self.assertEqual(self.problem.answer(self.list_1, self.list_2), self.expected_result, "Wrong sum!")


if __name__ == '__main__':
    unittest.main()
