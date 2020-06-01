import sys
class Solution:
    """
    @param prices: Given an integer array
    @return: Maximum profit
    """
    def maxProfit(self, prices):
        if not prices:
            return 0
        max_profit = 0
        for partition_i in range(len(prices)):
            left_max_profit = self.max_profit_in_partition(prices, 0, partition_i)
            right_max_profit = self.max_profit_in_partition(prices, partition_i + 1, len(prices) - 1)
            max_profit = max(max_profit, left_max_profit + right_max_profit)
        return max_profit

    def max_profit_in_partition(self, prices, start_index, ending_index):
        if not (0 <= start_index < len(prices) and 0 <= ending_index <= len(prices)):
            return 0
            
        smallest = sys.maxsize
        max_profit = -sys.maxsize
        for i in range(start_index, ending_index + 1):
            smallest = min(smallest, prices[i])
            max_profit = max(prices[i] - smallest, max_profit)
        return max_profit if max_profit > 0 else 0
        
    def build_smallest_number_from_left(self, prices):
        if not prices:
            return prices
            
        smallest_number_from_left = [prices[0]]
        for price in prices:
            last_price = smallest_number_from_left[-1]
            if price < last_price:
                smallest_number_from_left.append(price)
            else:
                smallest_number_from_left.append(last_price)
        return smallest_number_from_left
