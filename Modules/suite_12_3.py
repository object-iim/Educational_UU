import unittest
import tests_12_3

test_tests = unittest.TestSuite()
test_tests.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.RunnerTest))
test_tests.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(test_tests)