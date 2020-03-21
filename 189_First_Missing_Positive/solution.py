class Solution:
    """
    @param A: An array of integers
    @return: An integer
    """
    def firstMissingPositive(self, A):
        n = len(A)
        index = 0
        while index < n:
            position = A[index] - 1
            if position not in range(0, n) or position == index or A[position] == A[index]:
                index += 1
                continue
            A[index], A[position] = A[position], A[index]
                
        for index in range(n):
            if index != A[index] - 1 :
                return index + 1
        
        return n + 1