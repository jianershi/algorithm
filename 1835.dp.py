"""
dp[i][j] number of ways to go from steps i to location j
dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j] + dp[i - 1][j + 1]
intialization
dp[0][0] = 1
result dp[steps][0]
"""
# class Solution:
#     """
#     @param steps: steps you can move
#     @param arrLen: the length of the array
#     @return: Number of Ways to Stay in the Same Place After Some Steps
#     """
#     def numWays(self, steps, arrLen):
#         dp = [[0] * arrLen for _ in range(steps + 1)]
#         dp[0][0] = 1
#         for i in range(1, steps + 1):
#             for j in range(0, arrLen):
#                 dp[i][j] = dp[i - 1][j]
#                 if j > 0:
#                     dp[i][j] += dp[i - 1][j - 1]
#                 if j < arrLen - 1:
#                     dp[i][j] += dp[i - 1][j + 1]
#         print (dp[steps][0])
#         return dp[steps][0]
#
# s = Solution()
# steps = 15
# arrLen = 1000000
# s.numWays(steps, arrLen)


#drone pilot algorithm
#https://leetcode.com/problems/number-of-ways-to-stay-in-the-same-place-after-some-steps/discuss/622038/DP-Drone-Pilot-algorithm-DFS-%2B-memo-%2B-Drone-flying-nightmare
# class Solution:
#     """
#     @param steps: steps you can move
#     @param arrLen: the length of the array
#     @return: Number of Ways to Stay in the Same Place After Some Steps
#     """
#     def numWays(self, steps, arrLen):
#         arrLen = min(steps // 2 + 1, arrLen)
#         dp = [[0] * arrLen for _ in range(steps + 1)]
#         dp[0][0] = 1
#         for i in range(1, steps + 1):
#             for j in range(0, arrLen):
#                 dp[i][j] = dp[i - 1][j]
#                 if j > 0:
#                     dp[i][j] += dp[i - 1][j - 1]
#                 if j < arrLen - 1:
#                     dp[i][j] += dp[i - 1][j + 1]
#         print (dp[steps][0])
#         return dp[steps][0]

#rolling array algorithm
class Solution:
    """
    @param steps: steps you can move
    @param arrLen: the length of the array
    @return: Number of Ways to Stay in the Same Place After Some Steps
    """
    def numWays(self, steps, arrLen):
        arrLen = min(steps // 2 + 1, arrLen)
        dp = [[0] * arrLen for _ in range(2)]
        # dp1 = [0] * arrLen
        # dp2 = [0] * arrLen
        dp[0][0] = 1
        # dp2[0] = 1
        # dp[0][0] = 1
        for i in range(1, steps + 1):
            for j in range(0, arrLen):
                dp[i % 2][j] = dp[(i - 1) % 2][j]
                if j > 0:
                    dp[i % 2][j] += dp[(i - 1) % 2][j - 1]
                if j < arrLen - 1:
                    dp[i % 2][j] += dp[(i - 1) % 2][j + 1]
        # print (dp[steps % 2][0])
        return dp[steps % 2][0]

s = Solution()
steps = 15
arrLen = 1000000
s.numWays(steps, arrLen)
