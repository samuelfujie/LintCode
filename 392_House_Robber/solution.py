class Solution:
    """
    @param A: An array of non-negative integers
    @return: The maximum amount of money you can rob tonight
    """
    def houseRobber(self, A):
        if not A:
            return 0
        if len(A) <= 2:
            return max(A)
        
        # pp = previous of previous
        pp, p = A[0], max(A[0], A[1])
        for i in range(2, len(A)):
            cur = max(pp + A[i], p)
            pp = p
            p = cur
            
        return p