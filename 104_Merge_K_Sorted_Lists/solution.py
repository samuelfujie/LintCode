"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
import heapq
class Solution:
    """
    @param lists: a list of ListNode
    @return: The head of one sorted list.
    """
    def mergeKLists(self, lists):
        if not lists:
            return None
            
        # operator overload
        ListNode.__lt__ = lambda x, y: (x.val < y.val)
        
        dummy = ListNode(0)
        current = dummy
        heap = []
        
        for head in lists:
            if head is not None:
                heapq.heappush(heap, head)
        
        while heap:
            node = heapq.heappop(heap)
            current.next = node
            current = node
            if node.next:
                heapq.heappush(heap, node.next)

        return dummy.next