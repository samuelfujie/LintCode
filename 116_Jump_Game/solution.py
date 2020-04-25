class Solution:
    """
    @param A: A list of integers
    @return: A boolean
    """
    def canJump(self, A):
        n = len(A)

        furthest_i = current_i = 0

        while furthest_i < n - 1:
            if current_i > furthest_i:
                return False
            furthest_i = max(furthest_i, current_i + A[current_i])
            current_i += 1

        return True
