// Test cases
const testCases = [
  { arr: [2, 1, 5, 1, 3, 2], k: 3, expected: 9 },
  { arr: [2, 3, 4, 1, 5], k: 2, expected: 7 },
];

testCases.forEach(({ arr, k, expected }, index) => {
  const result = maxSubArrayOfSizeK(k, arr);
  console.assert(result === expected, `Test case ${index + 1} failed: Expected ${expected}, got ${result}`);
});
