"""
89. k Sum
https://www.lintcode.com/problem/k-sum/description?_from=ladder&&fromId=106
九章强化班

背包问题

dp[i][k][s] how many ways to choose k numbers out of previous i numbers to get target s

k is additional dimention because the question requires exactly k numbers

answer:
sum(dp[n][k][target])

initial condiiton
dp[i][0][0] = 1 # choose 0 number out of previous i number so that sum is 0: 1 way(not to choose at all)
dp[0][0][s] = 0 for s > 0

sliding array
"""
class Solution:
    """
    @param A: An integer array
    @param k: A positive integer (k <= length(A))
    @param target: An integer
    @return: An integer
    """
    def kSum(self, A, k, target):
        # write your code here
        n = len(A)

        dp = [[[0] * (target + 1) for _ in range(k + 1)] for _ in range(2)]

        old, now = 0, 0

        for s in range(1, target + 1):
            dp[now][0][s] = 0

        dp[now][0][0] = 1 # for dp[0][0][0] = 1
        
        for i in range(1, n + 1):
            old = now
            now = 1 - now
            dp[now][0][0] = 1 #move dp[i][0][0] = 1 initialization inside, because every i has to be initalized
            for j in range(1, k + 1):
                for s in range(1, target + 1):
                    dp[now][j][s] = dp[old][j][s]
                    if s >= A[i - 1]:
                        dp[now][j][s] += dp[old][j - 1][s - A[i - 1]]

        return dp[now][k][target]
