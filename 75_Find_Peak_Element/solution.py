class Solution:
    """
    @param A: An integers array.
    @return: return any of peek positions.
    """
    def findPeak(self, A):
        left, right = 0, len(A) - 1

        while left + 1 < right:
            mid = (left + right) // 2
            if A[mid] > A[mid + 1]:
                right = mid
            else:
                left = mid

        return left if A[left] > A[right] else right
