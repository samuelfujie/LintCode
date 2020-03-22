# 535. House Robber III
[ https://www.lintcode.com/problem/house-robber-iii/description ]

The thief has found himself a new place for his thievery again. There is only one entrance to this area, called the "root." Besides the root, each house has one and only one parent house. After a tour, the smart thief realized that "all houses in this place forms a binary tree". It will automatically contact the police if two directly-linked houses were broken into on the same night.

Determine the maximum amount of money the thief can rob tonight without alerting the police.

## Example
**Example 1:**

Input:
```sh
{3,2,3,#,3,#,1}
```
Output:
```sh
7
```
Explanation: Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.
```
  3
 / \
2   3
 \   \ 
  3   1
```

**Example 2:**

Input:
```sh
{3,4,5,1,3,#,1}
```
Output:
```sh
9
```
Explanation: Maximum amount of money the thief can rob = 4 + 5 = 9.
```
    3
   / \
  4   5
 / \   \ 
1   3   1
```

## Notice
This problem is the extention of [House Robber](https://www.lintcode.com/problem/house-robber/description) and [House Robber II](https://www.lintcode.com/problem/house-robber-ii/description).
