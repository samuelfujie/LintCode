class Solution:
    """
    @param nums: An array of non-negative integers.
    @return: The maximum amount of money you can rob tonight
    """
    def houseRobber2(self, A):
        if not A:
            return 0
        if len(A) <= 2:
            return max(A)
        
        pp, p = A[0], max(A[0], A[1])
        for i in range(2, len(A) - 1):
            cur = max(pp + A[i], p)
            pp, p = p, cur
        without_last = p
        
        pp, p = A[1], max(A[1], A[2])
        for i in range(3, len(A)):
            cur = max(pp + A[i], p)
            pp, p = p, cur
        without_first = p
        
        return max(without_first, without_last)