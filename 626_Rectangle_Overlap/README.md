# 626. Rectangle Overlap
[ https://www.lintcode.com/problem/rectangle-overlap/description ]

Given two rectangles, find if the given two rectangles overlap or not.

## Example
**Example 1:**

Input:
```sh
l1 = [0, 8], r1 = [8, 0], l2 = [6, 6], r2 = [10, 0]
```
Output:
```sh
true
```

**Example 2:**

Input:
```sh
l1 = [0, 8], r1 = [8, 0], l2 = [9, 6], r2 = [10, 0]
```
Output:
```sh
false
```

## Notice
- l1: Top Left coordinate of first rectangle.
- r1: Bottom Right coordinate of first rectangle.
- l2: Top Left coordinate of second rectangle.
- r2: Bottom Right coordinate of second rectangle.
- l1 != r1 and l2 != r2