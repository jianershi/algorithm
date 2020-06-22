"""
436. Maximal Square
https://www.lintcode.com/problem/maximal-square/description?_from=ladder&&fromId=106


dp[i][j] the maximum area for squres with lower right point ending in i,j
dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1 if matrix[i][j] == 1 else 0

initial condition:
dp[0][0] = matrix[i][j]
calculation direciton: left->right, up->down

answer
max dp[i][j]
"""
import sys
class Solution:
    """
    @param matrix: a matrix of 0 and 1
    @return: an integer
    """
    def maxSquare(self, matrix):
        # write your code here
        if not matrix or not matrix[0]:
            return 0
        n = len(matrix)
        m = len(matrix[0])

        dp = [[0] * m for _ in range(n)]

        for j in range(m):
            dp[0][j] = matrix[0][j]
        for i in range(n):
            dp[i][0] = matrix[i][0]

        for i in range(1, n):
            for j in range(1, m):
                if matrix[i][j] == 0:
                    dp[i][j] = 0
                    continue
                dp[i][j] = min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1]) + 1

        return max([max(x) for x in dp]) ** 2
