# 642. Moving Average from Data Stream
[ https://www.lintcode.com/problem/moving-average-from-data-stream/description ]

Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.

## Example
**Example 1:**

```sh
MovingAverage m = new MovingAverage(3);
m.next(1) = 1 // return 1.00000
m.next(10) = (1 + 10) / 2 // return 5.50000
m.next(3) = (1 + 10 + 3) / 3 // return 4.66667
m.next(5) = (10 + 3 + 5) / 3 // return 6.00000
```