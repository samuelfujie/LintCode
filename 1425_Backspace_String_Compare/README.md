# 1425. Backspace String Compare
[ https://www.lintcode.com/problem/backspace-string-compare/description ]

Given two strings `S` and `T`, return if they are equal when both are typed into empty text editors. `#` means a backspace character.

## Example
**Example 1:**

Input:
```sh
S = "ab#c", T = "ad#c"
```
Output:
```sh
true
```
Explanation: 
Both S and T become "ac".

**Example 2:**

Input:
```sh
S = "ab##", T = "c#d#"
```
Output:
```sh
true
```
Explanation: 
Both S and T become "".

**Example 3:**

Input:
```sh
S = "a##c", T = "#a#c"
```
Output:
```sh
true
```
Explanation: 
Both S and T become "c".

**Example 4:**

Input:
```sh
S = "a#c", T = "b"
```
Output:
```sh
false
```
Explanation: 
S becomes "c" while T becomes "b".

## Challenge
Can you solve it in `O(N)` time and `O(1)` space?

## Notice
- `1 <= S.length <= 200`
- `1 <= T.length <= 200`
- `S` and `T` only contain lowercase letters and `'#'` characters.