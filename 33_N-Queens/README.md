# 33. N-Queens
[ https://www.lintcode.com/problem/n-queens/description ]

The n-queens puzzle is the problem of placing n queens on an `n×n` chessboard such that no two queens attack each other(Any two queens can't be in the same row, column, diagonal line).

Given an integer `n`, return all distinct solutions to the n-queens puzzle.

Each solution contains a distinct board configuration of the n-queens' placement, where `'Q'` and `'.'` each indicate a queen and an empty space respectively.

## Example
Example 1:
Input:
```sh
1
```
Output:
```sh
[["Q"]]
```
Example 2:
Input:
```sh
4
```
Output:
```sh
[
  // Solution 1
  [".Q..",
   "...Q",
   "Q...",
   "..Q."
  ],
  // Solution 2
  ["..Q.",
   "Q...",
   "...Q",
   ".Q.."
  ]
]
```

## Challenge
Can you do it without recursion?