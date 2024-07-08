import unittest

class TestSmallestSubarraySum(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(smallest_subarray_sum(7, [2, 1, 5, 2, 3, 2]), 2)
        self.assertEqual(smallest_subarray_sum(7, [2, 1, 5, 2, 8]), 1)
        self.assertEqual(smallest_subarray_sum(8, [3, 4, 1, 1, 6]), 3)

# Manually create and run the test suite
def run_tests():
    suite = unittest.TestLoader().loadTestsFromTestCase(TestSmallestSubarraySum)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    return result

# Run the tests and capture the results
test_result = run_tests()
