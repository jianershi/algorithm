"""
110. Minimum Path Sum
https://www.lintcode.com/problem/minimum-path-sum/description

recursive function: dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]

initial condition:
dp[0][0] = grid[0][0]
dp[i][0]
dp[0][j]

answer:
dp[n - 1][m - 1]
"""
import sys
class Solution:
    """
    @param grid: a list of lists of integers
    @return: gridn integer, minimizes the sum of all numbers along its path
    """
    def minPathSum(self, grid):
        # write your code here
        if not grid or not grid[0]:
            return 0
        n = len(grid)
        m = len(grid[0])

        dp = [[sys.maxsize] * m for _ in range(n)]

        #intial condition
        dp[0][0] = grid[0][0]

        for i in range(n):
            for j in range(m):
                if i > 0:
                    dp[i][j] = min(dp[i][j], dp[i - 1][j] + grid[i][j])
                if j > 0:
                    dp[i][j] = min(dp[i][j], dp[i][j - 1] + grid[i][j])

        return dp[n - 1][m - 1]
