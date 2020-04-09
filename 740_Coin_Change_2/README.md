# 740. Coin Change 2
[ https://www.lintcode.com/problem/coin-change-2/description ]

You are given coins of different denominations and a total amount of money. Write a function to compute the number of combinations that make up that amount. You may assume that you have infinite number of each kind of coin.

## Example
**Example 1:**

Input:
```sh
amount = 10 and coins = [10] 
```
Output:
```sh
1
```

**Example 2:**

Input:
```sh
amount = 8 and coins = [2, 3, 8]
```
Output:
```sh
3
```
Explanation:
there are three ways to make up the amount:
8 = 8
8 = 3 + 3 + 2
8 = 2 + 2 + 2 + 2

## Notice
You can assume below:
- 0 <= amount <= 5000
- 1 <= coin <= 5000
- the number of coins is less than 500
- the answer is guaranteed to fit into signed 32-bit integer