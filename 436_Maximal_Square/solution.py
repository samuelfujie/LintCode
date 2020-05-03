class Solution:
    """
    @param matrix: a matrix of 0 and 1
    @return: an integer
    """
    def maxSquare(self, matrix):
        if not matrix or not matrix[0]:
            return 0

        row, col = len(matrix), len(matrix[0])
        dp = [[0] * col for _ in range(row)]
        max_side = 0

        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 0:
                    continue

                if i == 0 or j == 0:
                    dp[i][j] = matrix[i][j]
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1

                max_side = max(max_side, dp[i][j])

        return max_side ** 2
