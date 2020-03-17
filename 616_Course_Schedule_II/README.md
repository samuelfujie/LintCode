# 616. Course Schedule II
[ https://www.lintcode.com/problem/course-schedule-ii/description ]

There are a total of n courses you have to take, labeled from `0` to `n - 1`.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, return the ordering of courses you should take to finish all courses.

There may be multiple correct orders, you just need to return one of them. If it is impossible to finish all courses, return an empty array.

## Example
**Example 1:**

Input:
```sh
n = 2
prerequisites = [[1,0]] 
```
Output:
```sh
[0,1]
```

**Example 2:**

Input:
```sh
n = 4
prerequisites = [[1,0],[2,0],[3,1],[3,2]] 
```
Output:
```sh
[0,1,2,3] or [0,2,1,3]
```