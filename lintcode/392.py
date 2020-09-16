"""
392. House Robber
https://www.lintcode.com/problem/house-robber/description?_from=ladder&&fromId=106

535. House Robber III 在高频题班讲过。用divide and conquer

        do not rob current
        v
dp[i] = max(dp[i - 1], dp[i - 2] + A[i])
                        ----------------
                        ^ rob current

initial
dp[0] = A[0]
dp[1] = max(dp[0], A[1])

answer
dp[n - 1]
"""
class Solution:
    """
    @param A: An array of non-negative integers
    @return: The maximum amount of money you can rob tonight
    """
    def houseRobber(self, A):
        # write your code here
        if not A:
            return 0
        n = len(A)

        dp = [0] * n

        dp[0] = A[0]
        
        for i in range(1, n):
            dp[i] = dp[i - 1]
            if i == 1:
                dp[i] = max(dp[i], A[i])
            if i > 1:
                dp[i] = max(dp[i], dp[i - 2] + A[i])

        return dp[n - 1]
