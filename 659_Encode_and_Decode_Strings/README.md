# 659. Encode and Decode Strings
[ https://www.lintcode.com/problem/encode-and-decode-strings/description ]

Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.

Please implement `encode` and `decode`

## Example
**Example 1:**

Input:
```sh
["lint","code","love","you"]
```
Output:
```sh
["lint","code","love","you"]
```
Explanation:
One possible encode method is: 
```sh
"lint:;code:;love:;you"
```

**Example 2:**

Input:
```sh
["we", "say", ":", "yes"]
```
Output:
```sh
["we", "say", ":", "yes"]
```
Explanation:
One possible encode method is:
```sh
"we:;say:;:::;yes"
```