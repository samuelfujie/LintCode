"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
"""

class Solution:
    # @param {TreeNode} root the root of binary tree
    # @return {ListNode[]} a lists of linked list
    def binaryTreeToLists(self, root):
        output = []
        if root is None:
            return output
        
        queue = collections.deque([root])
        while queue:
            head = tail = None
            for _ in range(len(queue)):
                tree_node = queue.popleft()
                if tree_node:
                    list_ndoe = ListNode(tree_node.val)
                    if not head:
                        head = tail = list_ndoe
                    else:
                        tail.next = list_ndoe
                        tail = list_ndoe
                    queue.append(tree_node.left)
                    queue.append(tree_node.right)
            if head:
                output.append(head)
                
        return output