# Example 1
assert fruits_into_baskets(['A', 'B', 'C', 'A', 'C']) == 3

# Example 2
assert fruits_into_baskets(['A', 'B', 'C', 'B', 'B', 'C']) == 5

# Additional Test Cases

# Test Case 3: All same fruits
assert fruits_into_baskets(['A', 'A', 'A', 'A']) == 4

# Test Case 4: Each fruit is different
assert fruits_into_baskets(['A', 'B', 'C', 'D']) == 2

# Test Case 5: Long sequence with multiple best options
assert fruits_into_baskets(['A', 'B', 'A', 'B', 'C', 'B', 'B', 'C', 'D', 'E']) == 5

# Test Case 6: Empty array
assert fruits_into_baskets([]) == 0

# Test Case 7: Single type of fruit
assert fruits_into_baskets(['B', 'B', 'B']) == 3

# Test Case 8: Two types of fruit intermixed
assert fruits_into_baskets(['A', 'B', 'A', 'B', 'A', 'B']) == 6
