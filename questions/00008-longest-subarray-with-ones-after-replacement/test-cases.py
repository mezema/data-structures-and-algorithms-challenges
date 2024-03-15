# Example 1
assert length_of_longest_subarray([0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], 2) == 6

# Example 2
assert length_of_longest_subarray([0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1], 3) == 9

# Additional Test Cases

# Test Case 3: No replacements needed
assert length_of_longest_subarray([1, 1, 1, 1, 1], 2) == 5

# Test Case 4: Replace all zeros
assert length_of_longest_subarray([0, 0, 0, 0], 4) == 4

# Test Case 5: Empty array
assert length_of_longest_subarray([], 2) == 0

# Test Case 6: Array with all zeros
assert length_of_longest_subarray([0, 0, 0, 0, 0], 2) == 3

# Test Case 7: Array with alternating ones and zeros
assert length_of_longest_subarray([1, 0, 1, 0, 1, 0, 1], 2) == 5

# Test Case 8: Large k with mixed array
assert length_of_longest_subarray([1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 0], 4) == 10
