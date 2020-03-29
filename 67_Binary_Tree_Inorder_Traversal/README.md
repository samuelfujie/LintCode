# 67. Binary Tree Inorder Traversal
[ https://www.lintcode.com/problem/binary-tree-inorder-traversal/description ]

Given a binary tree, return the inorder traversal of its nodes' values.

## Example
**Example 1:**

Input:
```sh
{1,2,3}
```
Output:
```sh
[2,1,3]
```
Explanation: 
```sh
   1
  / \
 2   3
```
It will be serialized {1,2,3}

**Example 2:**

Input:
```sh
{1,#,2,3}
```
Output:
```sh
[1,3,2]
```
Explanation: 
```sh
 1
  \
   2
  /
 3
```
It will be serialized {1,#,2,3}

## Challenge
Can you do it without recursion?