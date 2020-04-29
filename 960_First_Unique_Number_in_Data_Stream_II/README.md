# 960. First Unique Number in Data Stream II
[ https://www.lintcode.com/problem/first-unique-number-in-data-stream-ii/description ]

We need to implement a data structure named `DataStream`. There are `two` methods required to be implemented:

1. `void add(number)` // add a new number
2. `int firstUnique()` // return first unique number

## Example
**Example 1:**

Input:
```sh
add(1)
add(2)
firstUnique()
add(1)
firstUnique()
```
Output:
```sh
[1,2]
```

**Example 2:**

Input:
```sh
add(1)
add(2)
add(3)
add(4)
add(5)
firstUnique()
add(1)
firstUnique()
add(2)
firstUnique()
add(3)
firstUnique()
add(4)
firstUnique()
add(5)
add(6)
firstUnique()
```
Output:
```sh
[1,2,3,4,5,6]
```

## Notice
You can assume that there must be at least one unique number in the stream when calling the firstUnique.