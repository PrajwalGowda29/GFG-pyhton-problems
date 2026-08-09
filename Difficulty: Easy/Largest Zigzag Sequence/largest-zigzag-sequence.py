class Solution:
    def zigzagSequence(self, mat):
        n = len(mat)

        dp = [[0] * n for _ in range(n)]

        # First row
        for j in range(n):
            dp[0][j] = mat[0][j]

        # Remaining rows
        for i in range(1, n):
            for j in range(n):
                best = 0

                for k in range(n):
                    if k != j:
                        best = max(best, dp[i - 1][k])

                dp[i][j] = mat[i][j] + best

        return max(dp[n - 1])