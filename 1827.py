"""
1827. Number of Ways to Stay in the Same Place After Some Steps II
SAME SOLUTION AS 1835
"""
# class Solution:
#     """
#     @param steps: steps you can move
#     @param arrLen: the length of the array
#     @return: Number of Ways to Stay in the Same Place After Some Steps
#     """
#     def numWays(self, steps, arrLen):
#         MOD = 1000000007
#         arrLen = min(steps // 2 + 1, arrLen)
#         dp = [[0] * arrLen for _ in range(2)]
#         # dp1 = [0] * arrLen
#         # dp2 = [0] * arrLen
#         dp[0][0] = 1
#         # dp2[0] = 1
#         # dp[0][0] = 1
#         for i in range(1, steps + 1):
#             for j in range(0, arrLen):
#                 dp[i % 2][j] = dp[(i - 1) % 2][j]
#                 if j > 0:
#                     dp[i % 2][j] = (dp[i % 2][j] % MOD + dp[(i - 1) % 2][j - 1] % MOD) % MOD
#                 if j < arrLen - 1:
#                     dp[i % 2][j] = (dp[i % 2][j] % MOD + dp[(i - 1) % 2][j + 1] % MOD) % MOD
#         # print (dp[steps % 2][0])
#         return dp[steps % 2][0] % MOD

# class Solution:
#     """
#     @param steps: steps you can move
#     @param arrLen: the length of the array
#     @return: Number of Ways to Stay in the Same Place After Some Steps
#     """
#     def numWays(self, steps, arrLen):
#         # write your code here
#         memo =  {} # index, curr_step
#         # print(memo)
#         return self.dfs(steps, arrLen, 0, steps, memo)
#
#     """
#     return true if curr_step is 0 and back in origin
#     return False otherwise
#     recursively go to 3 directions that is within range, need to have counter.
#     easisest way is to have global counter, but that is not very nice.
#     but is the easiest way.
#
#     divide and conquer, the total number of ways is the sum of ways of 3 directions.
#
#     """
#     def dfs(self, steps, arr_len, index, curr_step, memo):
#         MOD = 1000000007
#         if not (0 <= index < arr_len):
#             return 0
#         if (index, curr_step) in memo:
#             return memo[(index, curr_step)]
#         if curr_step == 0:
#             if index == 0:
#                 memo[(index, curr_step)] = 1
#             else:
#                 memo[(index, curr_step)] = 0
#             return memo[(index, curr_step)]
#
#         left_total = self.dfs(steps, arr_len, index - 1, curr_step - 1, memo) % MOD
#         right_total = self.dfs(steps, arr_len, index + 1, curr_step - 1, memo) % MOD
#         center_total = self.dfs(steps, arr_len, index, curr_step - 1, memo) % MOD
#         memo[(index, curr_step)] = (left_total + right_total + center_total) % MOD
#         return memo[(index, curr_step)]
