<!--info-header-start--><h1>Smallest Subarray With a Greater Sum <img src="https://img.shields.io/badge/-easy-ob6623" alt="easy"/> <img src="https://img.shields.io/badge/-%23arrays" alt="#arrays"/> <img src="https://img.shields.io/badge/-%23sliding--window-999" alt="#sliding-window"/></h1><blockquote><p>by Mark Ezema <a href="https://github.com/mezema" target="_blank">@mezema</a></p></blockquote><!--info-header-end-->

Given a string and a pattern, find **all anagrams of the pattern in the given string**.

Every **anagram** is a **permutation** of a string. As we know, when we are not allowed to repeat characters while finding permutations of a string, we get *N*! permutations (or anagrams) of a string having *N* characters. For example, here are the six anagrams of the string “abc”:

1. abc
2. acb
3. bac
4. bca
5. cab
6. cba

Write a function to return a list of starting indices of the anagrams of the pattern in the given string.

### Example 1:

- **Input:** String="ppqp", Pattern="pq"
- **Output:** [1, 2]
- **Explanation:** The two anagrams of the pattern in the given string are "pq" and "qp".

### Example 2:

- **Input:** String="abbcabc", Pattern="abc"
- **Output:** [2, 3, 4]
- **Explanation:** The three anagrams of the pattern in the given string are "bca", "cab", and "abc".

<!--info-footer-start--><br><a href="../../README.md" target="_blank"><img src="https://img.shields.io/badge/-Back-grey" alt="Back"/></a><!--info-footer-end-->