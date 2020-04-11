"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param root: a root of binary tree
    @return: return a integer
    """
    def diameterOfBinaryTree(self, root):
        if not root:
            return 0
        node_count, _ = self.dfs(root)
        diameter = node_count - 1
        return diameter

    def dfs(self, node):
        """
        @return: (max, path)
        max: the number of nodes on the longest link within the tree
        path: the number of nodes on the longest link that uses root as one end
        """
        if node is None:
            return 0, 0

        left_max, left_path = self.dfs(node.left)
        right_max, right_path = self.dfs(node.right)

        current_max = max(left_max, right_max, left_path + 1 + right_path)
        current_path = max(left_path, right_path) + 1

        return current_max, current_path
