# 12. Min Stack
[ https://www.lintcode.com/problem/min-stack/description ]

Implement a stack with following functions:

- `push(val)` push val into the stack
- `pop()` pop the top element and return it
- `min()` return the smallest number in the stack

All above should be in O(1) cost.

## Example
**Example 1:**

Input:
```sh
  push(1)
  pop()
  push(2)
  push(3)
  min()
  push(1)
  min()
```
Output:
```sh
1
2
1
```

**Example 2:**

Input:
```sh
  push(1)
  min()
  push(2)
  min()
  push(3)
  min()
```
Output:
```sh
1
1
1
```

## Notice
`min()` will never be called when there is no number in the stack.