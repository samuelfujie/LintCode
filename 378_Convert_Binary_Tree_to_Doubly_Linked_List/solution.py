"""
Definition of Doubly-ListNode
class DoublyListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = self.prev = nextDefinition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: The root of tree
    @return: the head of doubly list node
    """
    def bstToDoublyList(self, root):
        if not root:
            return root
    
        lst = []
        self.helper(root, lst)
        n = len(lst)
        for i in range(n):
            if i in range(0, n - 1):
                lst[i].next = lst[i + 1]
            if i in range(1, n):
                lst[i].prev = lst[i - 1]
        
        return lst[0]
        
    def helper(self, root, lst):
        if not root:
            return
        self.helper(root.left, lst)
        lst.append(DoublyListNode(root.val))
        self.helper(root.right, lst)