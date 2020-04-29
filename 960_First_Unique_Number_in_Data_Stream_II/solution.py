class DoublyLinkedListNode:
    def __init__(self, value=None):
        self.val = value
        self.prev = self.next = None


class DataStream:

    def __init__(self):
        # hash map
        self.val_to_node = {}
        # set
        self.duplicates = set([])
        # doubly linked list
        self.head = DoublyLinkedListNode()
        self.tail = DoublyLinkedListNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    """
    @param num: next number in stream
    @return: nothing
    """
    def add(self, num):
        if num not in self.duplicates:
            if num in self.val_to_node:
                evict_node = self.val_to_node[num]
                self.delete(evict_node)
                del self.val_to_node[num]
                self.duplicates.add(num)
            else:
                new_node = DoublyLinkedListNode(num)
                self.val_to_node[num] = new_node
                self.insert_left(new_node, self.tail)

    def insert_left(self, node, anchor):
        anchor.prev.next = node
        node.prev = anchor.prev
        node.next = anchor
        anchor.prev = node

    def delete(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        node.next = node.prev = None

    """
    @return: the first unique number in stream
    """
    def firstUnique(self):
        return self.head.next.val
