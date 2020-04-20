class Solution:
    """
    @param triangle: a list of lists of integers
    @return: An integer, minimum path sum
    """
    def minimumTotal(self, triangle):
        if not triangle:
            return 0

        n = len(triangle)
        dp = [[0] * n, [0] * n]
        dp[0][0] = triangle[0][0]

        for i in range(1, n):
            dp[i % 2][0] = dp[(i - 1) % 2][0] + triangle[i][0]
            for j in range(1, i):
                dp[i % 2][j] = min(dp[(i - 1) % 2][j], dp[(i - 1) % 2][j - 1]) + triangle[i][j]
            dp[i % 2][i] = dp[(i - 1) % 2][i - 1] + triangle[i][i]

        return min(dp[(n - 1) % 2])
