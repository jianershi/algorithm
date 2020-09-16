import sys
class Solution:
    """
    @param prices: Given an integer array
    @return: Maximum profit
    """
    def maxProfit(self, prices):
        smallest = sys.maxsize
        max_profit = -sys.maxsize
        for price in prices:
            smallest = min(smallest, price)
            max_profit = max(price - smallest, max_profit)
        return max_profit if max_profit > 0 else 0



s = Solution()
prices = [1, 2, 3, 4, 5]
print(s.maxProfit(prices))
