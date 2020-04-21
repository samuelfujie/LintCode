# 849. Basic Calculator III
[ https://www.lintcode.com/problem/basic-calculator-iii/description ]

Implement a basic calculator to evaluate a simple expression string.

The expression string may contain open `(` and closing parentheses `)`, the plus `+` or minus sign `-`, `non-negative` integers and empty spaces .

The expression string contains only non-negative integers, `+`, `-`, `*`, `/` operators , open `(` and closing parentheses `)` and empty spaces . The integer division should truncate toward zero.

You may assume that the given expression is always valid. All intermediate results will be in the range of `[-2147483648, 2147483647]`

## Example
**Example 1:**

Input:
```sh
"1 + 1"
```
Output:
```sh
2
```
Explanation：
1 + 1 = 2

**Example 2:**

Input:
```sh
" 6-4 / 2 "
```
Output:
```sh
4
```
Explanation：
6 - (4 / 2) = 4

## Notice
**Do not** use the `eval` built-in library function.