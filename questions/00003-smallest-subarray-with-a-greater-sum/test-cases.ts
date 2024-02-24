// Test cases
const testCases = [
  { arr: [2, 1, 5, 2, 3, 2], s: 7, expected: 2 },
  { arr: [2, 1, 5, 2, 8], s: 1, expected: 1 },
];

testCases.forEach(({ arr, s, expected }, index) => {
  const result = smallest_subarray_with_given_sum(arr, s);
  console.assert(result === expected, `Test case ${index + 1} failed: Expected ${expected}, got ${result}`);
});
