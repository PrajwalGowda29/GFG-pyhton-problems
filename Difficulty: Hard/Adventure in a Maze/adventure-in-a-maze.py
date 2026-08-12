class Solution:
    def findWays(self, grid):
        n = len(grid)
        MOD = 10**9 + 7

        paths = [[0] * n for _ in range(n)]
        adventure = [[0] * n for _ in range(n)]

        paths[0][0] = 1
        adventure[0][0] = grid[0][0]

        for i in range(n):
            for j in range(n):

                # If this cell cannot be reached, skip it
                if paths[i][j] == 0:
                    continue

                # Move Right
                if grid[i][j] == 1 or grid[i][j] == 3:
                    if j + 1 < n:
                        paths[i][j + 1] = (
                            paths[i][j + 1] + paths[i][j]
                        ) % MOD

                        adventure[i][j + 1] = max(
                            adventure[i][j + 1],
                            adventure[i][j] + grid[i][j + 1]
                        )

                # Move Down
                if grid[i][j] == 2 or grid[i][j] == 3:
                    if i + 1 < n:
                        paths[i + 1][j] = (
                            paths[i + 1][j] + paths[i][j]
                        ) % MOD

                        adventure[i + 1][j] = max(
                            adventure[i + 1][j],
                            adventure[i][j] + grid[i + 1][j]
                        )

        # No valid path
        if paths[n - 1][n - 1] == 0:
            return [0, 0]

        return [
            paths[n - 1][n - 1],
            adventure[n - 1][n - 1]
        ]