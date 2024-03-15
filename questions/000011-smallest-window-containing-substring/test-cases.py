# Example 1
assert find_substring("aabdec", "abc") == "abdec"

# Example 2
assert find_substring("aabdec", "abac") == "aabdec"

# Example 3
assert find_substring("abdbca", "abc") == "bca"

# Example 4
assert find_substring("adcad", "abc") == ""

print("All test cases for 'Smallest Window containing Substring' passed!")
