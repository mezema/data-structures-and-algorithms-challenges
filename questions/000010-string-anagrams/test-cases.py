# Example 1
assert find_string_anagrams("ppqp", "pq") == [1, 2]

# Example 2
assert find_string_anagrams("abbcabc", "abc") == [2, 3, 4]

# Additional Test Cases

# Test Case 3: Pattern longer than the string
assert find_string_anagrams("a", "abc") == []

# Test Case 4: No anagrams found
assert find_string_anagrams("abcd", "efg") == []

# Test Case 5: Repeating pattern characters
assert find_string_anagrams("aaabababab", "aab") == [0, 1, 2, 5, 6]

# Test Case 6: Entire string is an anagram of the pattern
assert find_string_anagrams("bca", "abc") == [0]
