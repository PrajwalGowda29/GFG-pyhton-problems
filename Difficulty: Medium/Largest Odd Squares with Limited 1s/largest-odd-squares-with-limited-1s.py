class Solution:
    def largestSquare(self, mat: list[list[int]], queries: list[list[int]], k: int) -> list[int]:
        n = len(mat)
        m = len(mat[0])

        # Prefix sum
        prefix = [[0] * (m + 1) for _ in range(n + 1)]

        for i in range(n):
            for j in range(m):
                prefix[i + 1][j + 1] = (
                    mat[i][j]
                    + prefix[i][j + 1]
                    + prefix[i + 1][j]
                    - prefix[i][j]
                )

        # Count number of 1s in a square
        def count_ones(r1, c1, r2, c2):
            return (
                prefix[r2 + 1][c2 + 1]
                - prefix[r1][c2 + 1]
                - prefix[r2 + 1][c1]
                + prefix[r1][c1]
            )

        ans = []

        for i, j in queries:

            # Maximum possible radius
            high = min(i, j, n - 1 - i, m - 1 - j)

            low = 0
            best = -1

            # Binary search
            while low <= high:
                mid = (low + high) // 2

                r1 = i - mid
                c1 = j - mid
                r2 = i + mid
                c2 = j + mid

                ones = count_ones(r1, c1, r2, c2)

                if ones <= k:
                    best = mid
                    low = mid + 1
                else:
                    high = mid - 1

            if best == -1:
                ans.append(-1)
            else:
                ans.append(2 * best + 1)

        return ans