import unittest
from test.problem_1_test import TestProblem1
from test.problem_2_test import TestProblem2
from test.problem_3_test import TestProblem3


def create_test_suite():

    test_suite = unittest.TestSuite()
    test_suite.addTest(TestProblem1("test_longest_substring"))
    test_suite.addTest(TestProblem2("test_alphabetical_order"))
    test_suite.addTest(TestProblem3("test_most_frequent_digit"))

    return test_suite


if __name__ == '__main__':

    suite = create_test_suite()
    runner = unittest.TextTestRunner()
    runner.run(suite)
