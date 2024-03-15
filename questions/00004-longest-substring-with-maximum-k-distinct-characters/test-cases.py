# Example 1
assert longest_substring_with_k_distinct("araaci", 2) == 4

# Example 2
assert longest_substring_with_k_distinct("araaci", 1) == 2

# Example 3
assert longest_substring_with_k_distinct("cbbebi", 3) == 5

# Example 4
assert longest_substring_with_k_distinct("cbbebi", 10) == 6

# Additional Test Cases

# Test Case 5: String with all distinct characters
assert longest_substring_with_k_distinct("abcdef", 2) == 2

# Test Case 6: String with repeating characters only
assert longest_substring_with_k_distinct("aaaaaa", 1) == 6

# Test Case 7: K is zero (edge case, might require handling based on interpretation)
# assert longest_substring_with_k_distinct("abcdef", 0) == 0

# Test Case 8: Long string with mixed characters
assert longest_substring_with_k_distinct("aabbccddeeff", 3) == 6

# Test Case 9: Non-alphabetic characters
assert longest_substring_with_k_distinct("123#12", 2) == 3
