# 1311. Lowest Common Ancestor of a Binary Search Tree
[ https://www.lintcode.com/problem/lowest-common-ancestor-of-a-binary-search-tree/description ]

Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.

According to the [definition of LCA on Wikipedia](https://en.wikipedia.org/wiki/Lowest_common_ancestor): “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow **a node to be a descendant of itself**).”

Given binary search tree: root = {6,2,8,0,4,7,9,#,#,3,5}

![bst](https://github.com/samuelfujie/LintCode/blob/master/1131_Lowest_Common_Ancestor_of_a_Binary_Search_Tree/bst.jpg?raw=true)

## Example
**Example 1:**

Input:
```sh
{6,2,8,0,4,7,9,#,#,3,5}
2
8
```
Output:
```sh
6
```
Explanation: 
The LCA of nodes 2 and 8 is 6.

**Example 2:**

Input:
```sh
{6,2,8,0,4,7,9,#,#,3,5}
2
4
```
Output:
```sh
2
```
Explanation: 
The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.

## Notice
* All of the nodes' values will be unique.
* p and q are different and both values will exist in the BST.