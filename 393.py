"""
393. Best Time to Buy and Sell Stock IV

dp[i][k][0] = max(dp[i - 1][k][0], dp[i - 1][k][1] + prices[i])
dp[i][k][1] = max(dp[i - 1][k][1], dp[i - 1][k - 1][0] - prices[i])

dp[-1][k][0] = 0
dp[-1][k][1] = -sys.maxsize
dp[i][0][0] = 0
dp[i][0][1] = -sys.maxsize

reference: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/discuss/108870/Most-consistent-ways-of-dealing-with-the-series-of-stock-problems

https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-iv/solution/yi-ge-tong-yong-fang-fa-tuan-mie-6-dao-gu-piao-w-5/
"""
import sys
class Solution:
    """
    @param K: An integer
    @param prices: An integer array
    @return: Maximum profit
    """
    def maxProfit(self, K, prices):
        # write your code here

        dp = [[[0] * 2 for _ in range(K + 1)] for _ in range(len(prices) + 1)]

        for i in range(1, len(prices) + 1):
            dp[i][0][0] = 0
            dp[i][0][1] = -sys.maxsize

        for k in range(K + 1):
            dp[0][k][0] = 0
            dp[0][k][1] = -sys.maxsize

        for i in range(1, len(prices) + 1):
            for k in range(1, K + 1):
                dp[i][k][0] = max(dp[i - 1][k][0], dp[i - 1][k][1] + prices[i - 1])
                dp[i][k][1] = max(dp[i - 1][k][1], dp[i - 1][k - 1][0] - prices[i - 1])

        return dp[len(prices)][K][0]

s = Solution()
K = 1
prices = [3, 2, 1]
print(s.maxProfit(K, prices))