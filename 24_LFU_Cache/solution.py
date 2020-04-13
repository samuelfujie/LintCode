import collections


class DoublelyListNode:
    def __init__(self, key, val, freq=0):
        self.key = key
        self.val = val
        self.freq = freq
        self.prev = self.next = None


class LFUCache:
    """
    @param: capacity: An integer
    """
    def __init__(self, capacity):
        self.capacity = capacity
        self.count = 0
        self.key_node = collections.defaultdict(int)
        self.freq_node = collections.defaultdict(int)
        # initialize the doubly-linked list
        self.head = DoublelyListNode(None, None)
        self.tail = DoublelyListNode(None, None)
        self.head.next = self.tail
        self.tail.prev = self.head
    """
    @param: key: An integer
    @param: value: An integer
    @return: nothing
    """
    def set(self, key, value):
        if self.capacity:
            if key in self.key_node:
                node = self.key_node[key]
                node.val = value
                self.touch(node)
            else:
                # evict last node when full
                if self.count == self.capacity:
                    evit_node = self.tail.prev
                    self.delete(evit_node)
                    del self.key_node[evit_node.key]
                    if self.freq_node[evit_node.freq] == evit_node:
                        self.freq_node[evit_node.freq] = None
                # insert new node
                new_node = DoublelyListNode(key, value)
                self.insert_left(self.tail, new_node)
                self.key_node[key] = new_node
                self.freq_node[0] = new_node
                self.touch(new_node)

    def touch(self, node):
        freq = node.freq
        anchor = None

        if self.freq_node[freq] == node:
            if node.next.freq == freq:
                self.freq_node[freq] = node.next
            else:
                self.freq_node[freq] = None
            anchor = node.next
        else:
            anchor = self.freq_node[freq]

        if self.freq_node[freq + 1]:
            anchor = self.freq_node[freq + 1]

        self.delete(node)
        self.insert_left(anchor, node)
        node.freq = freq + 1
        self.freq_node[freq + 1] = node

    """
    @param: key: An integer
    @return: An integer
    """
    def get(self, key):
        if key not in self.key_node:
            return - 1
        node = self.key_node[key]
        self.touch(node)
        return node.val

    def delete(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        node.prev = node.next = None
        self.count -= 1

    def insert_left(self, anchor, node):
        anchor.prev.next = node
        node.prev = anchor.prev
        anchor.prev = node
        node.next = anchor
        self.count += 1
