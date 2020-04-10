"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param head: A ListNode.
    @return: A boolean.
    """
    def isPalindrome(self, head):
        if not head or not head.next:
            return True
            
        # find the middle node
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # reverse the second half
        prev = None
        while slow:
            next = slow.next
            slow.next = prev
            prev = slow
            slow = next
        
        # check is palindrome from both end to middle
        while prev:
            if prev.val != head.val:
                return False
            prev = prev.next
            head = head.next
            
        return True