class Solution:
    """
    @param m: an Integer
    @param n: an Integer
    @return: the bitwise AND of all numbers in [m,n]
    """
    def rangeBitwiseAnd(self, m, n):
        shift = 0
        while m < n:
            m = m >> 1
            n = n >> 1
            shift += 1
        return m << shift
