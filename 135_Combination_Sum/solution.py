class Solution:
    """
    @param candidates: A list of integers
    @param target: An integer
    @return: A list of lists of integers
    """
    def combinationSum(self, candidates, target):
        results = []
        self.dfs(sorted(candidates), target, 0, [], results)
        return results
        
    def dfs(self, candidates, target, index, subset, results):
        if target < 0:
            return
        if target == 0:
            results.append(list(subset))
            return
        
        for i in range(index, len(candidates)):
            if i > 0 and candidates[i] == candidates[i - 1]:
                continue
            subset.append(candidates[i])
            self.dfs(candidates, target - candidates[i], i, subset, results)
            subset.pop()