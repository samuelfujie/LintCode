# 915. Inorder Predecessor in BST
[ https://www.lintcode.com/problem/inorder-predecessor-in-bst/description ]

Given a binary search tree and a node in it, find the in-order predecessor of that node in the BST.

## Example
**Example 1:**

Input:
```sh
root = {2,1,3}
p = 1
```
Output:
```sh
null
```

**Example 2:**

Input:
```sh
root = {2,1}
p = 2
```
Output:
```sh
1
```

## Notice
If the given node has no in-order predecessor in the tree, return `null`