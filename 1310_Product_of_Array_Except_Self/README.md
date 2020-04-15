# 1310. Product of Array Except Self
[ https://www.lintcode.com/problem/product-of-array-except-self/description ]

Given an array of n integers where n > 1, `nums`, return an array output such that `output[i]` is equal to the product of all the elements of `nums` except `nums[i]`.

## Example
**Example 1:**

Input:
```sh
[1,2,3,4]
```
Output:
```sh
[24,12,8,6]
```
Explanation:
2*3*4=24
1*3*4=12
1*2*4=8
1*2*3=6

**Example 2:**

Input:
```sh
[2,3,8]
```
Output:
```sh
[24,16,6]
```
Explanation:
3*8=24
2*8=16
2*3=6

## Challenge
Could you solve it with constant space complexity? (Note: The output array does not count as extra space for the purpose of space complexity analysis.)

## Notice
Solve it **without division** and in O(n).