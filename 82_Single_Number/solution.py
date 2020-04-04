class Solution:
    """
    @param A: An integer array
    @return: An integer
    """
    def singleNumber(self, A):
        res = 0
        for i in A:
            res = res ^ i
        return res