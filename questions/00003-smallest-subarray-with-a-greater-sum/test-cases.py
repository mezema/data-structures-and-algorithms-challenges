class TestSmallestSubarraySum(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(smallest_subarray_sum(7, [2, 1, 5, 2, 3, 2]), 2)
        self.assertEqual(smallest_subarray_sum(7, [2, 1, 5, 2, 8]), 1)
        self.assertEqual(smallest_subarray_sum(8, [3, 4, 1, 1, 6]), 3)

    def test_additional_cases(self):
        self.assertEqual(smallest_subarray_sum(100, [1, 2, 3, 4, 5]), 0)
        self.assertEqual(smallest_subarray_sum(4, [1, 2, 3, 4, 5]), 1)
        self.assertEqual(smallest_subarray_sum(15, [1, 2, 3, 4, 5]), 5)
        self.assertEqual(smallest_subarray_sum(10, [1, 2, 3, 4, 5, 6]), 2)
        self.assertEqual(smallest_subarray_sum(9, [1, 2, 8, 4, 3]), 1)

if __name__ == "__main__":
    unittest.main()
