class MinStack:
    def __init__(self):
        self.stack = []

    """
    @param: number: An integer
    @return: nothing
    """
    def push(self, x):
        if self.stack:
            current_min = self.min()
            self.stack.append((x, min(x, current_min)))
        else:
            self.stack.append((x, x))

    """
    @return: An integer
    """
    def pop(self):
        if self.stack:
            val, _ = self.stack.pop()
            return val

    """
    @return: An integer
    """
    def min(self):
        if self.stack:
            return self.stack[-1][1]
