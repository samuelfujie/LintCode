class Solution:
    """
    @param m: an integer
    @param n: an integer
    @param ops: List[List[int]]
    @return: return an integer
    """
    def maxCount(self, m, n, ops):
        for a, b in ops:
            m = min(a, m)
            n = min(b, n)
        return m * n