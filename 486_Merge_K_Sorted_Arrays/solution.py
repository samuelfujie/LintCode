import heapq
class Solution:
    """
    @param arrays: k sorted integer arrays
    @return: a sorted array
    """
    def mergekSortedArrays(self, arrays):
        results = []
        if not arrays:
            return results
        
        heap = []
        for index, array in enumerate(arrays):
            if array:
                heapq.heappush(heap, (array[0], index, 0))
        
        while heap:
            val, arr_i, ele_i = heapq.heappop(heap)
            results.append(val)
            if ele_i + 1 < len(arrays[arr_i]):
                heapq.heappush(heap, (arrays[arr_i][ele_i + 1], arr_i, ele_i + 1))
        
        return results