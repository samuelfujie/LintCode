# 135. Combination Sum
[ https://www.lintcode.com/problem/combination-sum/description ]

Given a set of candidtate numbers `candidates` and a target number `target`. Find all unique combinations in `candidates` where the numbers sums to `target`.

The **same** repeated number may be chosen from `candidates` unlimited number of times.

## Example
**Example 1:**

Input:
```sh
candidates = [2, 3, 6, 7], target = 7
```
Output:
```sh
[[7], [2, 2, 3]]
```

**Example 2:**

Input:
```sh
candidates = [1], target = 3
```
Output:
```sh
[[1, 1, 1]]
```

## Notice
- All numbers (including `target`) will be positive integers.
- Numbers in a combination `a1, a2, … , ak` must be in non-descending order. (ie, `a1 ≤ a2 ≤ … ≤ ak`)
- Different combinations can be in any order.
- The solution set must not contain duplicate combinations.