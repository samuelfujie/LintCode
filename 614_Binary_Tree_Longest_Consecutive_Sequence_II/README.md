# 614. Binary Tree Longest Consecutive Sequence II
[ https://www.lintcode.com/problem/binary-tree-longest-consecutive-sequence-ii/description ]

Given a binary tree, find the length(number of nodes) of the longest consecutive sequence(Monotonic and adjacent node values differ by 1) path.

The path could be start and end at any node in the tree

## Example
**Example 1:**

Input:
```sh
{1,2,0,3}
```
Output:
```sh
4
```
Explanation:
```sh
    1
   / \
  2   0
 /
3
```
0-1-2-3

**Example 2:**

Input:
```sh
{3,2,2}
```
Output:
```sh
2
```
Explanation:
```sh
    3
   / \
  2   2
```
2-3