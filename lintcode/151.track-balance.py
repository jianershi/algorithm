"""
151. Best Time to Buy and Sell Stock III
method is written by Tin
source: https://www.jiuzhang.com/solution/best-time-to-buy-and-sell-stock-iii/#tag-other


only using current balance to track decision, the goal is to maximize balance
"""
import sys
class Solution:
    """
    @param prices: Given an integer array
    @return: Maximum profit
    """
    def maxProfit(self, prices):
        if not prices:
            return 0

        hold_1 = hold_2 = -max(prices)
        sold_1 = sold_2 = 0

        for price in prices:
            hold_1 = max(hold_1, -price)
            sold_1 = max(sold_1, hold_1 + price)
            hold_2 = max(hold_2, sold_1 - price)
            sold_2 = max(sold_2, hold_2 + price)
        return sold_2
