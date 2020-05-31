"""
暴力dp写法，时间复杂度o(n^2)过不了
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
                #print (dp)
                if dp[j % len(gas)] < 0:
                    skip_rest = True
                    start_position = j
                    #print(j)
                    break
            if skip_rest:
                continue
            possible = True
            for i in range(len(dp)):
                if dp[i] < 0:
                    possible = False
                    break
            if possible and dp[start_position] >= 0:
                return start_position
            start_position += 1
        return -1

s = Solution()
gas = [1,2,3,3]
cost = [2,1,5,1]

print(s.canCompleteCircuit(gas, cost))
