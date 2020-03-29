"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: A Tree
    @return: Preorder in ArrayList which contains node values.
    """
    
    """
    Solution 1: Recursion
    """
    def preorderTraversal(self, root):
        if root is None:
            return []
        left = self.preorderTraversal(root.left)
        right = self.preorderTraversal(root.right)
        return [root.val] + left + right
        
    """
    Solution 2: Iterative
    """
    def preorderTraversal(self, root):
        if root is None:
            return []
        stack = [root]
        results = []
        while stack:
            node = stack.pop()
            if node:
                results.append(node.val)
                stack.append(node.right)
                stack.append(node.left)
        return results