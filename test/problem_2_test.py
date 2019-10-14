import unittest
from answers.problem_2 import Problem2


class TestProblem2(unittest.TestCase):

    def setUp(self):
        self.problem = Problem2()
        self.inputs = (
            ([""], [""]),
            (["January", "February", "Mar", "Apr", "May", "June", "Jul", "august", "Sep", "Oct", "nov", "December"],
             ["august", "Apr", "December", "February", "January", "Jul", "June", "Mar", "May", "nov", "Oct", "Sep"])
        )

    @unittest.skip("Incomplete")
    def test_alphabetical_order(self):
        for input_data, expected_result in self.inputs:
            with self.subTest(input_data=input_data, expected_result=expected_result):
                self.assertEqual(self.problem.answer(input_data), expected_result, "Wrong sort!")


if __name__ == '__main__':
    unittest.main()
