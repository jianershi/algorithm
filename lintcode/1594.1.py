"""
1594. Maximum Non Negative Product in a Matrix
https://leetcode.com/contest/weekly-contest-207/problems/maximum-non-negative-product-in-a-matrix/
2 dp, 1 keep min, 1 keep max
"""
class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        MOD = 1000000007

        dp_max = [[0] * m for _ in range(n)]
        dp_min = [[0] * m for _ in range(n)]

        dp_min[0][0] = dp_max[0][0] = grid[0][0]

        #initialize top line and left line
        for i in range(1, n):
            dp_min[i][0] = dp_max[i][0] = dp_max[i - 1][0] * grid[i][0]
        for j in range(1, m):
            dp_min[0][j] = dp_max[0][j] = dp_max[0][j - 1] * grid[0][j]

        for i in range(1, n):
            for j in range(1, m):
                if grid[i][j] >= 0:
                    dp_max[i][j] = max(dp_max[i][j - 1], dp_max[i - 1][j]) * grid[i][j]
                    dp_min[i][j] = min(dp_min[i][j - 1], dp_min[i - 1][j]) * grid[i][j]
                else:
                    dp_max[i][j] = min(dp_min[i][j - 1], dp_min[i - 1][j]) * grid[i][j]
                    dp_min[i][j] = max(dp_max[i][j - 1], dp_max[i - 1][j]) * grid[i][j]

        return dp_max[n - 1][m - 1] % MOD if dp_max[n - 1][m - 1] >= 0 else -1

