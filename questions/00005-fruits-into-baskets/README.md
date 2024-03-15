<!--info-header-start--><h1>Smallest Subarray With a Greater Sum <img src="https://img.shields.io/badge/-easy-ob6623" alt="easy"/> <img src="https://img.shields.io/badge/-%23arrays" alt="#arrays"/> <img src="https://img.shields.io/badge/-%23sliding--window-999" alt="#sliding-window"/></h1><blockquote><p>by Mark Ezema <a href="https://github.com/mezema" target="_blank">@mezema</a></p></blockquote><!--info-header-end-->

You are visiting a farm to collect fruits. The farm has a single row of fruit trees. You will be given two baskets, and your goal is to pick as many fruits as possible to be placed in the given baskets.

You will be given an array of characters where each character represents a fruit tree. The farm has the following restrictions:

1. Each basket can have only one type of fruit. There is no limit to how much fruit a basket can hold.
2. You can start with any tree, but you can’t skip a tree once you have started.
3. You will pick exactly one fruit from every tree until you cannot, i.e., you will stop when you have to pick from a third fruit type.

Write a function to return the maximum number of fruits in both baskets.

### Example 1:

- **Input:** Fruit=['A', 'B', 'C', 'A', 'C']
- **Output:** 3
- **Explanation:** We can put 2 'C' in one basket and one 'A' in the other from the subarray ['C', 'A', 'C'].

### Example 2:

- **Input:** Fruit=['A', 'B', 'C', 'B', 'B', 'C']
- **Output:** 5
- **Explanation:** We can put 3 'B' in one basket and two 'C' in the other basket. This can be done if we start with the second letter: ['B', 'C', 'B', 'B', 'C']

<!--info-footer-start--><br><a href="../../README.md" target="_blank"><img src="https://img.shields.io/badge/-Back-grey" alt="Back"/></a><!--info-footer-end-->