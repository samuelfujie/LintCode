# 615. Course Schedule
[ https://www.lintcode.com/problem/course-schedule/description ]

There are a total of n courses you have to take, labeled from `0` to `n - 1`.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

## Example
**Example 1:**

Input:
```sh
n = 2
prerequisites = [[1,0]] 
```
Output:
```sh
true
```

**Example 2:**

Input:
```sh
n = 2
prerequisites = [[1,0],[0,1]] 
```
Output:
```sh
false
```