# 685. First Unique Number in Data Stream
[ https://www.lintcode.com/problem/first-unique-number-in-data-stream/description ]

Given a continuous stream of data, write a function that returns the first unique number (including the last number) when the terminating number arrives. If the unique number is not found, return `-1`.

## Example
**Example 1:**

Input:
```sh
[1, 2, 2, 1, 3, 4, 4, 5, 6]
5
```
Output:
```sh
3
```

**Example 2:**

Input:
```sh
[1, 2, 2, 1, 3, 4, 4, 5, 6]
7
```
Output:
```sh
-1
```

**Example 3:**

Input:
```sh
[1, 2, 2, 1, 3, 4]
3
```
Output:
```sh
3
```