# 1675. Super Maze
[ https://www.lintcode.com/problem/super-maze/description ]

Given a `maze` consisting of the numbers `0` and `1`, where `0` indicate the empty space and `1` indicate the obstacle. You can only move to four adjacent grids per move. You can now choose a point from `start[][]` as the start point. Choose one of the `end[][]` as the end point, output how many steps it takes to finish the maze at least.

It is guaranteed that the start point and the end point must be on the empty space, and there must be a solution in this problem.

## Example
**Example 1:**

Input:
```sh
maze = [
[0,0,0,0,0,0,0],
[1,0,0,1,0,0,0],
[0,0,1,0,1,0,0],
[0,0,0,1,0,0,0],
[0,0,0,0,1,0,0],
[0,0,0,0,1,0,1],
[0,1,0,0,0,0,0]],
start = [[2,5],[4,2],[3,4]],
end = [[0,5],[3,0]]
```
Output:
```sh
2
```
Explanation:
we choose (2, 5) to be the start point, and (0, 5) to be the end point, we need to move 2 steps at least.

**Example 2:**

Input:
```sh
maze = [
[0,1,0,0],
[0,0,0,1],
[0,1,0,1],
[1,0,1,1]
],
start = [[0,0],[3,1]],
end = [[1,1],[0,2]]
```
Output:
```sh
2
```
Explanation:
we choose (0, 0) to be the start point, and (1, 1) to be the end point, we need to move 2 steps at least.

## Notice
- the size of maze <= 200000
- len(starts), len(endd) <= 10000