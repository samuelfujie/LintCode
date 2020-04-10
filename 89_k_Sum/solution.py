import collections
class Solution:
    """
    @param A: An integer array
    @param k: A positive integer (k <= length(A))
    @param target: An integer
    @return: An integer
    """
    def kSum(self, A, k, target):
        # dp[i][j][t]: in first (i) number we pick (j) numbres whose sum is (t)
        # dp[i][j][t] = dp[i - 1][j][t] + dp[i - 1][j - 1][t - num[i]]
        dp = collections.defaultdict(lambda: collections.defaultdict(lambda: collections.defaultdict(int)))
        dp[0][0][0] = 1

        A.sort()
        # from the first 1 to n numbers
        for i in range(1, len(A) + 1):
            # we selected 0 to k of them
            for j in range(min(i + 1, k + 1)):
                # whose sum is 0 to target
                for t in range(target + 1):
                    current_num = A[i-1]
                    dp[i][j][t] = dp[i-1][j][t] + dp[i-1][j-1][t-current_num]

        # return select k number in array whose sum is target
        return dp[len(A)][k][target]
