"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the root of binary tree
    @return: the length of the longest consecutive sequence path
    """
    def __init__(self):
        self.max_len = 0
        
    def longestConsecutive2(self, root):
        inc, dec = self.dfs(root)
        return self.max_len
    
    def dfs(self, root):
        if root is None:
            return 0, 0
    
        li, ld = self.dfs(root.left)
        ri, rd = self.dfs(root.right)
        
        inc, dec = 1, 1
        if root.left:
            if root.left.val + 1 == root.val:
                inc = max(inc, li + 1)
            if root.left.val - 1 == root.val:
                dec = max(dec, ld + 1)
        if root.right:
            if root.right.val + 1 == root.val:
                inc = max(inc, ri + 1)
            if root.right.val - 1 == root.val:
                dec = max(dec, rd + 1)

        self.max_len = max(self.max_len, inc + dec - 1)
        return inc, dec