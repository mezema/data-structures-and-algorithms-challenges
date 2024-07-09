def run_tests(smallest_subarray_sum):
    # Define test cases: (input_array, target_sum, expected_output)
    test_cases = [
        ([2, 1, 5, 2, 3, 2], 7, 2),
        ([2, 1, 5, 2, 8], 7, 1),
        ([3, 4, 1, 1, 6], 8, 3),
        ([1, 1, 1, 1, 1], 5, 5),
        ([1, 2, 3, 4, 5], 15, 5),
        ([1, 2, 3, 4, 5], 20, 0),
        ([], 5, 0)
    ]
    
    # Run tests
    for i, (arr, s, expected) in enumerate(test_cases, 1):
        result = smallest_subarray_sum(arr, s)
        status = "PASS" if result == expected else "FAIL"
        print(f"Test Case {i}:")
        print(f"  Input: arr = {arr}, s = {s}")
        print(f"  Expected Output: {expected}")
        print(f"  Actual Output: {result}")
        print(f"  Status: {status}")
        print()
run_tests(smallest_subarray_sum)
