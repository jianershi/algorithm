"""
89. k Sum

"""
class Solution:
    """
    @param A: An integer array
    @param k: A positive integer (k <= length(A))
    @param target: An integer
    @return: An integer
    """
    def kSum(self, A, K, target):
        # write your code here
        dp = [[[0] * (target + 1) for _ in range(K + 1)] for _ in range(len(A) + 1)]

        # for t in range(target + 1):
        #     if A[0] == t:
        #         dp[0][1][t] = 1
        for i in range(len(A) + 1):
            dp[i][0][0] = 1

        for i in range(1, len(A) + 1):
            for k in range(1, K + 1):
                for t in range(1, target + 1):
                    dp[i][k][t] = dp[i - 1][k][t]
                    if t >= A[i - 1]:
                        dp[i][k][t] += dp[i - 1][k - 1][t - A[i - 1]]

        return (dp[len(A)][K][target])
