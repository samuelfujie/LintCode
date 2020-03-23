"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the root
    @param k: an integer
    @return: the value of the nearest leaf node to target k in the tree
    """
    def __init__(self):
        self.target = None
        self.parent = {}
    
    def findClosestLeaf(self, root, k):
        def getParents(node):
            if node:
                if node.val == k:
                    self.target = node
                if node.left:
                    self.parent[node.left] = node
                    getParents(node.left)
                if node.right:
                    self.parent[node.right] = node
                    getParents(node.right)
        getParents(root)

        from collections import deque
        q = deque([self.target])
        visited = set([self.target])
        while q:
            node = q.popleft()
            if node.left is None and node.right is None:
                return node.val
            if node.left and node.left not in visited:
                q.append(node.left)
            if node.right and node.right not in visited:
                q.append(node.right)
            if node in self.parent and self.parent[node] not in visited:
                q.append(self.parent[node])
            visited.add(node)
        
        return -1