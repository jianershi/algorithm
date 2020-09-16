"""
根据393.3 DP模版改写

"""
import sys
class Solution:
    """
    @param K: An integer
    @param prices: An integer array
    @return: Maximum profit
    """
    def maxProfit(self, prices):
        if len(prices) < 2:
            return 0

        dp = [[0] * 2 for _ in range(2)]

        for i in range(1, len(prices) + 1):
            dp[i % 2][0] = 0
            dp[i % 2][1] = -sys.maxsize

        for i in range(1, len(prices) + 1):
            dp[i % 2][0] = max(dp[(i - 1) % 2][0], dp[(i - 1) % 2][1] + prices[i - 1])
            dp[i % 2][1] = max(dp[(i - 1) % 2][1], dp[(i - 1) % 2][0] - prices[i - 1])

        return dp[len(prices) % 2][0]

s = Solution()
K = 1
prices = [3, 2, 1]
print(s.maxProfit(K, prices))
