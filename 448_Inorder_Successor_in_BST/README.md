# 448. Inorder Successor in BST
[ https://www.lintcode.com/problem/inorder-successor-in-bst/description ]

Given a binary search tree and a node in it, find the in-order successor of that node in the BST.

If the given node has no in-order successor in the tree, return `null`.

## Example
**Example 1:**

Input:
```sh
{1,#,2}
1
```
Output:
```sh
2
```
Explanation: 
```sh
  1
   \
    2
```

**Example 2:**

Input:
```sh
{2,1,3}
1
```
Output:
```sh
2
```
Explanation: 
```sh
    2
   / \
  1   3
```

## Challenge
O(h), where h is the height of the BST.

## Notice
It's guaranteed p is one node in the given tree. (You can directly compare the memory address to find p)