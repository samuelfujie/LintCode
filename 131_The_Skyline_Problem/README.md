# 131. The Skyline Problem
[ https://www.lintcode.com/problem/the-skyline-problem/description ]

Given N buildings in a x-axis，each building is a rectangle and can be represented by a triple (start, end, height)，where start is the start position on x-axis, end is the end position on x-axis and height is the height of the building. Buildings may overlap if you see them from far away，find the outline of them。

An outline can be represented by a triple, (start, end, height), where start is the start position on x-axis of the outline, end is the end position on x-axis and height is the height of the outline.

![skyline](https://github.com/samuelfujie/LintCode/blob/master/131_The_Skyline_Problem/skyline.jpg?raw=true)

## Example
**Example 1:**

Input:
```sh
    [1, 3, 3],
    [2, 4, 4],
    [5, 6, 1]
```
Output:
```sh
    [1, 2, 3],
    [2, 4, 4],
    [5, 6, 1]
```
Explanation: The buildings are look like this in the picture. The yellow part is buildings.

![example1](https://github.com/samuelfujie/LintCode/blob/master/131_The_Skyline_Problem/example1.jpg?raw=true)

**Example 2:**

Input:
```sh
    [1, 4, 3],
    [6, 9, 5]
```
Output:
```sh
    [1, 4, 3],
    [6, 9, 5]
```
Explanation: The buildings are look like this in the picture. The yellow part is buildings.

![example2](https://github.com/samuelfujie/LintCode/blob/master/131_The_Skyline_Problem/example2.jpg?raw=true)

## Notice
Please merge the adjacent outlines if they have the same height and make sure different outlines cant overlap on x-axis.