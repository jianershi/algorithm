"""
117. Jump Game II
https://www.lintcode.com/problem/jump-game-ii/description
dp[i]: min steps to readch position i

dp[i] = min(dp[j] + 1 if A[j] >= i - j) for all j 0 < j < i

intial condition
dp[0] = 0


result dp[n - 1]

这题不用动态规划也行。。
因为第一个j一定是最少部数到达i的。
dp = dp[j] + 1也能过。这边break也是同一个意思

"""
import sys
class Solution:
    """
    @param A: A list of integers
    @return: An integer
    """
    def jump(self, A):
        # write your code here
        if not A:
            return -1
        n = len(A)
        dp = [sys.maxsize] * n

        dp[0] = 0

        for i in range(1, n):
            for j in range(i):
                if A[j] >= i - j:
                    dp[i] = min(dp[i], dp[j] + 1)
                    break
                    
        return dp[n - 1]
