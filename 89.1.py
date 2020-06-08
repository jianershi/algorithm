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
        dp = [[[0] * (target + 1) for _ in range(K + 1)] for _ in range(2)]

        for t in range(target + 1):
            if A[0] == t:
                dp[0 % 2][1][t] = 1
        for i in range(len(A)):
            dp[i % 2][0][0] = 1

        for i in range(1, len(A)):
            for k in range(1, K + 1):
                for t in range(1, target + 1):
                    dp[i % 2][k][t] = dp[(i - 1) % 2][k][t]
                    if t >= A[i]:
                        dp[i % 2][k][t] += dp[(i - 1) % 2][k - 1][t - A[i]]

        return (dp[(len(A) - 1) % 2][K][target])

s = Solution()
A = [1,2,3,4]
K = 2
target=5
print(s.kSum(A,K,target))
