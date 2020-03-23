"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the root of tree
    @return: the vertical order traversal
    """
    def __init__(self):
        self.lookup = collections.defaultdict(lambda: collections.defaultdict(list))
        
    def verticalOrder(self, root):
        results = []
        if not root:
            return results
        
        self.travese(root, 0, 0)
        for x in sorted(self.lookup):
            vertical_list = []
            for y in sorted(self.lookup[x]):
                vertical_list += self.lookup[x][y]
            results.append(list(vertical_list))
        return results
        
    def travese(self, node, x, y):
        if node:
            self.lookup[x][y].append(node.val)
            self.travese(node.left, x - 1, y + 1)
            self.travese(node.right, x + 1, y + 1)