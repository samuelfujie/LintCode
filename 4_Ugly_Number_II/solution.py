import heapq
class Solution:
    """
    @param n: An integer
    @return: return a  integer as description.
    """
    def nthUglyNumber(self, n):
        heap = [1]
        heapq.heapify(heap)
        visited = set(heap)
        
        ans = None
        for _ in range(n):
            ans = heapq.heappop(heap)
            for factor in [2, 3, 5]:
                if ans * factor not in visited:
                    visited.add(ans * factor)
                    heapq.heappush(heap, ans * factor)
                    
        return ans