# 486. Merge K Sorted Arrays
[ https://www.lintcode.com/problem/merge-k-sorted-arrays/description ]

Given k sorted integer arrays, merge them into one sorted array.

## Example
**Example 1:**

Input:
```sh
  [
    [1, 3, 5, 7],
    [2, 4, 6],
    [0, 8, 9, 10, 11]
  ]
```
Output:
```sh
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
```

**Example 2:**

Input:
```sh
  [
    [1,2,3],
    [1,2]
  ]
```
Output:
```sh
[1,1,2,2,3]
```

## Challenge
Do it in O(N log k).