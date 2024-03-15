# Example 1
assert length_of_longest_substring("aabccbb", 2) == 5

# Example 2
assert length_of_longest_substring("abbcb", 1) == 4

# Example 3
assert length_of_longest_substring("abccde", 1) == 3

# Additional Test Cases

# Test Case 4: No replacements needed
assert length_of_longest_substring("aaaabbbb", 2) == 8

# Test Case 5: Replace all characters to one type
assert length_of_longest_substring("abcd", 4) == 4

# Test Case 6: Empty string
assert length_of_longest_substring("", 2) == 0

# Test Case 7: Single character string
assert length_of_longest_substring("aaaaa", 1) == 5

# Test Case 8: All characters need to be replaced and not enough replacements
assert length_of_longest_substring("abcde", 1) == 2

print("All test cases passed!")
