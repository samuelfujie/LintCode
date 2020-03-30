# 242. Convert Binary Tree to Linked Lists by Depth
[ https://www.lintcode.com/problem/convert-binary-tree-to-linked-lists-by-depth/description ]

Given a binary tree, design an algorithm which creates a linked list of all the nodes at each depth (e.g., if you have a tree with depth D, you'll have D linked lists).

## Example
**Example 1:**

Input:
```sh
{1,2,3,4}
```
Output:
```sh
[1->null,2->3->null,4->null]
```
Explanation: 
```
        1
       / \
      2   3
     /
    4
```

**Example 2:**

Input:
```sh
{1,#,2,3}
```
Output:
```sh
[1->null,2->null,3->null]
```
Explanation: 
```
    1
     \
      2
     /
    3
```