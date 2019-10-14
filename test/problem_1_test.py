import unittest
from answers.problem_1 import Problem1


class TestProblem1(unittest.TestCase):

    def setUp(self):
        self.problem = Problem1()

        self.inputs = (
            ("abcabcbb", ["bca", "abc", "cab"]),
            ("zzzzz", ["z"]),
            ("abbcdb", ["bcd", "cdb"]),
            ("", []),
            ("Aab", ["ab"])
        )

    def test_longest_substring(self):
        for input_data, expected_result in self.inputs:
            with self.subTest(input_data=input_data, expected_result=expected_result):
                self.assertCountEqual(self.problem.answer(input_data), expected_result, "Wrong answer!")


if __name__ == '__main__':
    unittest.main()
