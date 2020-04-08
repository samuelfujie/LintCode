"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param head: the head of linked list.
    @return: a middle node of the linked list
    """
    def middleNode(self, head):
        if head is None or head.next is None:
            return head
        
        dummy = ListNode(0)
        dummy.next = head

        slow, fast = dummy, dummy
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
        return slow