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
    @return: Inorder in ArrayList which contains node values.
    """
    
    """
    Solution 1: Recursion
    """
    def inorderTraversal(self, root):
        if root is None:
            return []
        left = self.inorderTraversal(root.left)
        right = self.inorderTraversal(root.right)
        return left + [root.val] + right

    """
    Solution 2: Iterative
    """
    def inorderTraversal(self, root):
        results = []
        if not root:
            return results
        
        stack = []
        current = root
    
        while current or stack:
            while current:
                stack.append(current)
                current = current.left
            current = stack.pop()
            results.append(current.val)
            current = current.right
                
        return results

    """
    Solution 3: Morris Inorder Traversal
    """
    def inorderTraversal(self, root):
        results = []
        if not root:
            return results
        self.morris(root, results)
        return results
        
    def morris(self, root, results):
        curr = root 
        while curr: 
            # If left child is null, print the 
            # current node data. And, update  
            # the current pointer to right child. 
            if curr.left is None: 
                results.append(curr.val)
                curr = curr.right 
            else: 
                # Find the inorder predecessor 
                prev = curr.left 
                while prev.right and prev.right is not curr: 
                    prev = prev.right 
  
                # If the right child of inorder 
                # predecessor already points to 
                # the current node, update the  
                # current with it's right child 
                if prev.right is curr: 
                    prev.right = None
                    results.append(curr.val)
                    curr = curr.right 
                  
                # else If right child doesn't point 
                # to the current node, then print this 
                # node's data and update the right child 
                # pointer with the current node and update 
                # the current with it's left child 
                else: 
                    prev.right = curr  
                    curr = curr.left 