# Example 1
assert non_repeat_substring("aabccbb") == 3

# Example 2
assert non_repeat_substring("abbbb") == 2

# Example 3
assert non_repeat_substring("abccde") == 3

# Additional Test Cases

# Test Case 4: All characters are distinct
assert non_repeat_substring("abcdef") == 6

# Test Case 5: Only one character, repeating
assert non_repeat_substring("aaaaaa") == 1

# Test Case 6: Empty string
assert non_repeat_substring("") == 0

# Test Case 7: Long string with mixed characters
assert non_repeat_substring("aabcdeffghijklmnopqrstuvwxyzz") == 26

# Test Case 8: String with non-alphabetic characters
assert non_repeat_substring("a1b2c3d4e5f6g7h8i9j0") == 20
