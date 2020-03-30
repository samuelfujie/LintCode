"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: root of a tree
    @return: head node of a doubly linked list
    """
    def treeToDoublyList(self, root):
        if not root:
            return root
            
        head, tail = self.helper(root)
        head.left = tail
        tail.right = head
        
        return head
    
    def helper(self, root):
        if root is None:
            return None, None
        
        left_head, left_tail = self.helper(root.left)
        right_head, right_tail = self.helper(root.right)
        
        head = tail = root
        if left_head:
            left_tail.right = root
            root.left = left_tail
            head = left_head
        if right_tail:
            right_head.left = root
            root.right = right_head
            tail = right_tail
        
        return head, tail