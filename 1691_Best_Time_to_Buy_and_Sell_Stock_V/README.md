# 1691. Best Time to Buy and Sell Stock V
[ https://www.lintcode.com/problem/best-time-to-buy-and-sell-stock-v ]

Given a stock `n`-day price, you can only trade at most once a day, you can choose to buy a stock or sell a stock or give up the trade today, output the maximum profit can reach.

## Example
**Example 1:**

Input:
```sh
[1,2,10,9]
```
Output:
```sh
16
```

**Example 2:**

Input:
```sh
source = "adobecodebanc", target = "abc"
```
Output:
```sh
"banc"
```
Explanation:
you can buy in day 1,2 and sell in 3,4.
profit:-1-2+10+9 = 16 

**Example 3:**

Input:
```sh
[9,5,9,10,5]
```
Output:
```sh
5
```
Explanation: 
you can buy in day 2 and sell in 4.
profit:-5 + 10 = 5

## Notice
`1 ≤ n ≤ 10000`