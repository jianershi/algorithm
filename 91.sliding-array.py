"""
91. Minimum Adjustment Cost
https://www.lintcode.com/problem/minimum-adjustment-cost/description

definition
dp[i][j]: minimum cost to change ith position to number k.

recurssive function
dp[i][j] = A[i] - j + min(dp[i - 1][k] for k in range(j-target, j+target))
dp[i][j] = min(dp[i][j], dp[i - 1][k] + A[i] - j) for k in range(j - target, j + target + 1)

initial condition:
dp[0][j] = abs(A[0] - j)

calculation direction:


answer:
min(dp[n - 1][j]) for all j

to change any number, it is not necessary to change it smaller than min and bigger than max

sliding array

"""
import sys
class Solution:
    """
    @param: A: An integer array
    @param: target: An integer
    @return: An integer
    """
    def MinAdjustmentCost(self, A, target):
        # write your code here
        if not A:
            return A
            
        n = len(A)
        min_number, max_number = min(A), max(A)
        dp = [[sys.maxsize] * (max_number + 1) for _ in range(2)]

        old = 1
        now = 0
        for i in range(n):
            for j in range(min_number, max_number + 1):
                dp[now][j] = sys.maxsize
                if i == 0:
                    dp[0][j] = abs(A[0] - j)
                for k in range(max(min_number, j - target), min(j + target + 1, max_number + 1)):
                    dp[now][j] = min(dp[now][j], dp[old][k] + abs(A[i] - j))
            old = now
            now = 1 - now
        
        return min(dp[old])