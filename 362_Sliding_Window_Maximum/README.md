# 362. Sliding Window Maximum
[ https://www.lintcode.com/problem/sliding-window-maximum/description ]

Given an array of n integer with duplicate number, and a moving window(size k), move the window at each iteration from the start of the array, find the maximum number inside the window at each moving.

## Example
**Example 1:**

Input:
```sh
[1,2,7,7,8]
3
```
Output:
```sh
[7,7,8]
```
Explanation：
At first the window is at the start of the array like this `[|1, 2, 7| ,7, 8]` , return the maximum `7`;
then the window move one step forward.`[1, |2, 7 ,7|, 8]`, return the maximum `7`;
then the window move one step forward again.`[1, 2, |7, 7, 8|]`, return the maximum `8`;

**Example 2:**

Input:
```sh
[1,2,3,1,2,3]
5
```
Output:
```sh
[3,3]
```
Explanation:
At first, the state of the window is as follows: ` [,2,3,1,2,1 | , 3] `, a maximum of ` 3 `;
And then the window to the right one. ` [1, | 2,3,1,2,3 |] `, a maximum of ` 3 `;

## Challenge
o(n) time and O(k) memory