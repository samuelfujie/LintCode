# 58. 4Sum
[ https://www.lintcode.com/problem/4sum/description ]

Given an array S of n integers, are there elements a, b, c, and d in S such that `a + b + c + d = target`?

Find all unique quadruplets in the array which gives the sum of target.

## Example
**Example 1:**

Input:
```sh
[2,7,11,15]
3
```
Output:
```sh
[]
```

**Example 2:**

Input:
```sh
[1,0,-1,0,-2,2]
0
```
Output:
```sh
[[-1, 0, 0, 1],[-2, -1, 1, 2],[-2, 0, 0, 2]]
```

## Notice
- Elements in a quadruplet (a,b,c,d) must be in non-descending order. (ie, a ≤ b ≤ c ≤ d)
- The solution set must not contain duplicate quadruplets.