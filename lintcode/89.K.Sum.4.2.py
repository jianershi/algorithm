"""
89. k Sum
https://www.lintcode.com/problem/k-sum/description?_from=ladder&&fromId=106
九章强化班

背包问题

dp[i][s][k] how many ways to choose k numbers out of previous i numbers to get target s
k is additional dimention because the question requires exactly k numbers

answer:
dp[n][target][k]

initial condiiton
dp[i][0][0] = 1 # choose 0 number out of previous i number so that sum is 0: 1 way(not to choose at all)

transfer:
dp[i][s][k] = dp[i - 1][s - A[i - 1]][k - 1] if A[i - 1] is choosen
            + dp[i - 1][s][k] if A[i - 1] is not choosen

"""
from typing import (
    List,
)

class Solution:
    """
    @param a: An integer array
    @param k: A positive integer (k <= length(A))
    @param target: An integer
    @return: An integer
    """
    def k_sum(self, a: List[int], k: int, target: int) -> int:
        # write your code here

        dp = [[[0] * (k + 1) for _ in range(target + 1)] for _ in range(2)]

        old, now = 0, 0
        #initialization
        for i in range(2):
            dp[i][0][0] = 1
        
        for i in range(1, len(a) + 1):
            for j in range(1, target + 1):
                for c in range(1, k + 1):
                    dp[i % 2][j][c] = dp[(i - 1) % 2][j][c]
                    if j >= a[i - 1]:
                        dp[i % 2][j][c] += dp[(i - 1) % 2][j - a[i - 1]][c - 1]
        
        return dp[len(a) % 2][target][k]