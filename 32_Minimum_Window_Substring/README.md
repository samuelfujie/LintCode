# 32. Minimum Window Substring
[ https://www.lintcode.com/problem/minimum-window-substring/description ]

Given two strings `source` and `target`. Return the minimum substring of `source` which contains each char of `target`.

## Example
**Example 1:**

Input:
```sh
source = "abc", target = "ac"
```
Output:
```sh
"abc"
```

**Example 2:**

Input:
```sh
source = "adobecodebanc", target = "abc"
```
Output:
```sh
"banc"
```
Explanation: 
"banc" is the minimum substring of source string which contains each char of target "abc".

**Example 3:**

Input:
```sh
source = "abc", target = "aa"
```
Output:
```sh
""
```
Explanation: 
No substring contains two 'a'.

## Challenge
O(n) time

## Notice
- If there is no answer, return `""`.
- You are guaranteed that the answer is unique.
- `target` may contain duplicate char, while the answer need to contain at least the same number of that char.