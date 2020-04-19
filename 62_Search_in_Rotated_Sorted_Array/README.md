# 62. Search in Rotated Sorted Array
[ https://www.lintcode.com/problem/search-in-rotated-sorted-array/description ]

Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., `0 1 2 4 5 6 7` might become `4 5 6 7 0 1 2`).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

## Example
**Example 1:**

Input:
```sh
[4, 5, 1, 2, 3]
target=1
```
Output:
```sh
2
```

**Example 2:**

Input:
```sh
[4, 5, 1, 2, 3]
target=0
```
Output:
```sh
-1
```

## Challenge
O(logN) time