"""
187. Gas Station
https://www.lintcode.com/problem/gas-station/description
"""
class Solution:
    """
    @param gas: An array of integers
    @param cost: An array of integers
    @return: An integer
    """
    def canCompleteCircuit(self, gas, cost):
        # write your code here

        #iterate through all starting positions
        start_position = 0
        while start_position < len(gas):
            skip_rest = False
            dp = [None] * len(gas)
            dp[start_position] = 0
            for j in range(start_position + 1, start_position + len(gas) + 1):
                dp[j % len(gas)] = dp[(j - 1) % len(gas)] + gas[(j - 1) % len(gas)] - cost[(j - 1) % len(gas)]
                if dp[j % len(gas)] < 0:
                    skip_rest = True
                    start_position = j
                    break
            if skip_rest:
                continue
            if dp[start_position] >= 0:
                return start_position
            start_position += 1
        return -1