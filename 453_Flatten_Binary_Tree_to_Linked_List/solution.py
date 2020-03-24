"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: a TreeNode, the root of the binary tree
    @return: nothing
    """
    def flatten(self, root):
        self.helper(root)
        return

    def helper(self, root):
        if root is None:
            return None
            
        left_end = self.helper(root.left)
        right_end = self.helper(root.right)
        
        if left_end:
            left_end.right = root.right
            root.right = root.left
            root.left = None
        
        return right_end or left_end or root