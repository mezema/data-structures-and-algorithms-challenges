# Example 1
assert smallest_subarray_with_given_sum(7, [2, 1, 5, 2, 3, 2]) == 2

# Example 2
assert smallest_subarray_with_given_sum(7, [2, 1, 5, 2, 8]) == 1

# Example 3
assert smallest_subarray_with_given_sum(8, [3, 4, 1, 1, 6]) == 3

# Additional Test Cases

# Test Case 4: No such subarray exists
assert smallest_subarray_with_given_sum(100, [1, 2, 3, 4, 5]) == 0

# Test Case 5: Single element satisfies the condition
assert smallest_subarray_with_given_sum(4, [1, 2, 3, 4, 5]) == 1

# Test Case 6: Entire array is the smallest subarray satisfying the condition
assert smallest_subarray_with_given_sum(15, [1, 2, 3, 4, 5]) == 5

# Test Case 7: Small subarray at the end
assert smallest_subarray_with_given_sum(10, [1, 2, 3, 4, 5, 6]) == 2

# Test Case 8: Small subarray in the middle
assert smallest_subarray_with_given_sum(9, [1, 2, 8, 4, 3]) == 1
