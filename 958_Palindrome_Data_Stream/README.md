# 958. Palindrome Data Stream
[ https://www.lintcode.com/problem/palindrome-data-stream/description ]

There is a data stream, one letter at a time, and determine whether the current stream's **arrangement** can form a palindrome.

## Example
**Example 1:**

Input:
```sh
s = ['a','a','a','a','a']
```
Output:
```sh
[1,1,1,1,1]
```
Explanation: 
“a” can form a palindrome
“aa” can form a palindrome
“aaa” can form a palindrome
“aaaa” can form a palindrome
“aaaaa” can form a palindrome

**Example 2:**

Input:
```sh
s = ['a','b','a']
```
Output:
```sh
[1,0,1]
```
Explanation: 
“a” can form a palindrome
“ab” can't form a palindrome
“aba” can form a palindrome

## Notice
`1 <= |s| <= 10^5`