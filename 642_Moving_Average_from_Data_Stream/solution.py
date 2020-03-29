from collections import deque
class MovingAverage:
    """
    @param: size: An integer
    """
    def __init__(self, size):
        self.capacity = size
        self.window = deque([])
        self.total = 0

    """
    @param: val: An integer
    @return:  
    """
    def next(self, val):
        self.window.append(val)
        self.total += val
        if len(self.window) > self.capacity:
            self.total -= self.window.popleft()
        return self.total / len(self.window)

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param = obj.next(val)