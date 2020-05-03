"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
import sys


class Solution:
    """
    @param root: The root of binary tree.
    @return: An integer
    """
    def maxPathSum(self, root):
        if not root:
            return root

        max_path_sum, _ = self.helper(root)

        return max_path_sum

    def helper(self, root):
        if not root:
            return -sys.maxsize-1, -sys.maxsize-1

        left_max, left_ended = self.helper(root.left)
        right_max, right_ended = self.helper(root.right)

        root_ended = max(0, left_ended, right_ended) + root.val
        root_cross = max(0, left_ended) + max(0, right_ended) + root.val
        root_max = max(left_max, right_max, root_cross)

        return root_max, root_ended
