# Test Case 1: Given examples
assert max_sub_array_of_size_k(3, [2, 1, 5, 1, 3, 2]) == 9
assert max_sub_array_of_size_k(2, [2, 3, 4, 1, 5]) == 7

# Test Case 2: Small array where array length is equal to k
assert max_sub_array_of_size_k(3, [1, 2, 3]) == 6

# Test Case 3: Single-element array
assert max_sub_array_of_size_k(1, [5]) == 5

# Test Case 4: k is nearly the size of the array
assert max_sub_array_of_size_k(4, [1, 2, 3, 4, 5]) == 14

# Test Case 5: All elements are the same
assert max_sub_array_of_size_k(3, [4, 4, 4, 4, 4]) == 12