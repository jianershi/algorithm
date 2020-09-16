"""
隔板法。
先建立2个list,
smallest_before[i] : 原数列index i 之前的最小值。
largest_after[i]: 原数列index i 之后的最大值。
这2个都可以事先独立计算每个花费O(n)

然后隔板遍历从左到右。分别寻找左区间最小值和有区间最大值。
隔板遍历本身需要O(n),但是左区间最小值和右区间最大值已经算过了。只需要O(1)时间查询。

总体时间复杂度O(n)。但是实际上遍历了3次。时间上不是最优的。
这个方法可以运用到pen box
"""
import sys
class Solution:
    """
    @param prices: Given an integer array
    @return: Maximum profit
    """
    def maxProfit(self, prices):
        # write your code here
        if not prices:
            return 0
        smallest_before = self.find_smallest_before(prices)
        largest_after = [-a for a in self.find_smallest_before([-x for x in prices][::-1])[::-1]]

        max_profit = -sys.maxsize
        for k in range(0, len(prices)):
            #k 可以同时包括在前后区间。。因为你可以当天买了就卖了。
            max_profit = max(max_profit, largest_after[k] - smallest_before[k])
        return max_profit if max_profit > 0 else 0

    """
    smallest_before[i] is the smallest number before index i in the original prices list
    """
    def find_smallest_before(self, prices):
        smallest = [sys.maxsize] * len(prices)
        smallest[0] = prices[0]
        for i in range(1, len(prices)):
            smallest[i] = min(smallest[i - 1], prices[i])
        return smallest

s = Solution()
prices = [5]
print(s.maxProfit(prices))
