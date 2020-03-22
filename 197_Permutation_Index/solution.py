import math
class Solution:
    """
    @param A: An array of integers
    @return: A long integer
    """
    def permutationIndex(self, A):
        n = len(A)
        # count how many permutation before A
        permutation_counter = 0
        for i in reversed(range(len(A) - 1)):
            smaller_num_counter = self.counterSmallerNumber(A[i], A[i+1:])
            permutation_counter += math.factorial(n - 1 - i) * smaller_num_counter
        return permutation_counter + 1
        
    def counterSmallerNumber(self, target, nums):
        count = 0
        for num in nums:
            if num < target:
                count += 1
        return count