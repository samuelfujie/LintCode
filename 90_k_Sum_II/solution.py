class Solution:
    """
    @param: A: an integer array
    @param: k: a postive integer <= length(A)
    @param: targer: an integer
    @return: A list of lists of integer
    """
    def kSumII(self, A, k, target):
        results = []
        if A is None:
            return results
        self.dfs(A, k, target, results, [], 0)
        return results
    
    def dfs(self, A, k, target, results, subset, index):
        if len(subset) == k:
            if sum(subset) == target:
                results.append(list(subset))
            return
            
        for i in range(index, len(A)):
            subset.append(A[i])
            self.dfs(A, k, target, results, subset, i + 1)
            subset.pop()