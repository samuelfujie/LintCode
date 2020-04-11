# 1181. Diameter of Binary Tree
[ https://www.lintcode.com/problem/diameter-of-binary-tree/description ]

Given a binary tree, you need to compute the length of the diameter of the tree. The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

## Example
**Example 1:**

Input:
```sh
          1
         / \
        2   3
       / \     
      4   5  
```
Output:
```sh
3
```
Explanation:
the length of the path [4,2,1,3] or [5,2,1,3]

**Example 2:**

Input:
```sh
[2,3,#,1]
```
Output:
```sh
2
```
Explanation:
```sh
      2
    /
   3
 /
1
```

## Notice
The length of path between two nodes is represented by the number of edges between them.