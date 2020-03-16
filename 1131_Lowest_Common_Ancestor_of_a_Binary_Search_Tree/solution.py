"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
from collections import deque
class Solution:
    """
    @param root: root of the tree
    @param p: the node p
    @param q: the node q
    @return: find the LCA of p and q
    """
    
    # Solution 1: Binary Tree
    def lowestCommonAncestor(self, root, p, q):
        if root is None or root == p or root == q:
            return root
        
        leftLCA = self.lowestCommonAncestor(root.left, p, q)
        rightLCA = self.lowestCommonAncestor(root.right, p, q)
        
        if leftLCA and rightLCA:
            return root
        
        if leftLCA is not None:
            return leftLCA
        return rightLCA
        
    # Solution 2: Binary Search Tree
    def lowestCommonAncestor(self, root, p, q):
        if root.val < min(p.val, q.val):
            return self.lowestCommonAncestor(root.right, p, q)
        
        if root.val > max(p.val, q.val):
            return self.lowestCommonAncestor(root.left, p, q)
            
        # if root == p or root == q
        #    or min(p, q) < root < max(p, q)
        return root