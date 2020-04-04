class MyQueue:
    
    def __init__(self):
        self.push_stack = []
        self.pop_stack = []

    """
    @param: element: An integer
    @return: nothing
    """
    def push(self, element):
        self.push_stack.append(element)

    """
    @return: An integer
    """
    def pop(self):
        if self.pop_stack:
            return self.pop_stack.pop()
        self.dump()
        return self.pop_stack.pop()

    """
    @return: An integer
    """
    def top(self):
        if self.pop_stack:
            return self.pop_stack[-1]
        self.dump()
        return self.pop_stack[-1]
    
    def dump(self):
        while self.push_stack:
            self.pop_stack.append(self.push_stack.pop())