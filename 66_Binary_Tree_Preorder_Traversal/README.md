# 66. Binary Tree Preorder Traversal
[ https://www.lintcode.com/problem/binary-tree-preorder-traversal/description ]

Given a binary tree, return the preorder traversal of its nodes' values.

## Example
**Example 1:**

Input:
```sh
{1,2,3}
```
Output:
```sh
[1,2,3]
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
[1,2,3]
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

## Notice
- The first data is the root node, followed by the value of the left and right son nodes, and "#" indicates that there is no child node.
- The number of nodes does not exceed 20.