# 512. Decode Ways
[ https://www.lintcode.com/problem/decode-ways/description ]

A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26

Given an encoded message containing digits, determine the total number of ways to decode it.

## Example
**Example 1:**

Input:
```sh
"12"
```
Output:
```sh
2
```
Explanation: It could be decoded as AB (1 2) or L (12).

**Example 2:**

Input:
```sh
"10"
```
Output:
```sh
1
```

## Notice
If given string is empty, return `0`.