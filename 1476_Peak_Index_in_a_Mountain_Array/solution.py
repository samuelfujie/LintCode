class Solution:
    """
    @param A: an array
    @return: any i such that A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1]
    """
    def peakIndexInMountainArray(self, A):
        left, right = 0, len(A) - 1

        while left + 1 < right:
            mid = (left + right) // 2
            if A[mid] > A[mid + 1]:
                right = mid
            else:
                left = mid

        return left if A[left] > A[right] else right
