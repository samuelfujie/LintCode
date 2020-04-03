import heapq
class Solution:
    """
    @param a: the array a
    @return: return the maximum profit
    """
    def getAns(self, a):
        if not a:
            return 0
        
        profit = 0    
        heap = []
        heapq.heapify(heap)
        for price in a:
            if heap and heap[0] < price:
                profit += price - heapq.heappop(heap)
                heapq.heappush(heap, price)
            heapq.heappush(heap, price)
        
        return profit