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
    @return: Postorder in ArrayList which contains node values.
    """
    
    """
    Solution 1: Recursion
    """
    def postorderTraversal(self, root):
        if not root:
            return []
        left = self.postorderTraversal(root.left)
        right = self.postorderTraversal(root.right)
        return left + right + [root.val]
    
    """
    Solution 2: Iterative to simulate reverse_postorder
    """
    def postorderTraversal(self, root):
        results = []
        if not root:
            return results
            
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                results.append(node.val)
                # if use deque to push front
                # then no need to return reversedr results
                stack.append(node.left)
                stack.append(node.right)
        
        return results[::-1]