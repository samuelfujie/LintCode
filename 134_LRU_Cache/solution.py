class LinkedNode:
    def __init__(self, key=None, value=None, prev=None, next=None):
        self.key = key
        self.val = value
        self.prev = prev
        self.next = next

class LRUCache:
    """
    @param: capacity: An integer
    """
    def __init__(self, capacity):
        self.max_capacity = capacity
        self.key_to_node = {}
        self.head = None
        self.tail = None

    """
    @param: key: An integer
    @return: An integer
    """
    def get(self, key):
        if key not in self.key_to_node:
            return -1
        node = self.key_to_node[key]
        self.mostFrequentUse(node)
        return node.val
        
    """
    @param: key: An integer
    @param: value: An integer
    @return: nothing
    """
    def set(self, key, value):
        if key in self.key_to_node:
            node = self.key_to_node[key]
            node.val = value
            self.mostFrequentUse(node)
        else:
            new_node = LinkedNode(key, value)
            
            if len(self.key_to_node) == 0:
                self.head = new_node
                self.tail = new_node
            else:
                if len(self.key_to_node) == self.max_capacity:
                    del self.key_to_node[self.tail.key]
                    self.tail = self.tail.prev
                new_node.next = self.head
                self.head.prev = new_node
                self.head = new_node
    
            self.key_to_node[key] = new_node
    
    def mostFrequentUse(self, node):
        if self.head == node:
            return
        
        if self.tail == node:
            self.tail = node.prev
            
        node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev
            
        node.next = self.head
        self.head.prev = node
        self.head = node
        node.prev = None