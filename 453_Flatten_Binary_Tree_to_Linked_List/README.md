# 453. Flatten Binary Tree to Linked List
[ https://www.lintcode.com/problem/flatten-binary-tree-to-linked-list/description ]

Flatten a binary tree to a fake "linked list" in pre-order traversal.

Here we use the right pointer in TreeNode as the next pointer in ListNode.

## Example
**Example 1:**

Input:
```sh
{1,2,5,3,4,#,6}
```
Output:
```sh
{1,#,2,#,3,#,4,#,5,#,6}
```
Explanation: 
```sh
     1
    / \
   2   5
  / \   \
 3   4   6

1
\
 2
  \
   3
    \
     4
      \
       5
        \
         6
```

**Example 2:**

Input:
```sh
{1}
```
Output:
```sh
{1}
```
Explanation: 
```sh
    1
    1
```

## Challenge
Do it in-place without any extra memory.

## Notice
Don't forget to mark the left child of each node to null. Or you will get Time Limit Exceeded or Memory Limit Exceeded.