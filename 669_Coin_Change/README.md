# 669. Coin Change
[ https://www.lintcode.com/problem/coin-change/description ]

You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return `-1`.

## Example
**Example 1:**

Input:
```sh
[1, 2, 5]
11
```
Output:
```sh
3
```
Explanation: 
11 = 5 + 5 + 1

**Example 2:**

Input:
```sh
[2]
3
```
Output:
```sh
-1
```

## Notice
- You may assume that you have an infinite number of each kind of coin.
- It is guaranteed that:
    - the num of money will not exceed 10000
    - the num of coins wii not exceed 500
    - the denomination of each coin will not exceed 100