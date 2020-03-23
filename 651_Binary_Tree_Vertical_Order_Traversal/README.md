# 651. Binary Tree Vertical Order Traversal
[ https://www.lintcode.com/problem/binary-tree-vertical-order-traversal/description ]

Given a binary tree, return the vertical order traversal of its nodes' values. (ie, from top to bottom, column by column).

If two nodes are in the same row and column, the order should be from **left to right**.

## Example
**Example 1:**

Input:
```sh
{3,9,20,#,#,15,7}
```
Output:
```sh
[[9],[3,15],[20],[7]]
```
Explanation: 
```sh
   3
  /\
 /  \
 9  20
    /\
   /  \
  15   7
```

**Example 2:**

Input:
```sh
{3,9,8,4,0,1,7}
```
Output:
```sh
[[4],[9],[3,0,1],[8],[7]]
```
Explanation: 
```sh
     3
    /\
   /  \
   9   8
  /\  /\
 /  \/  \
 4  01   7
```