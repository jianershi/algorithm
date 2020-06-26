"""
593. Stone Game II
https://www.lintcode.com/problem/stone-game-ii/description?_from=ladder&&fromId=106


cancellation type of problem: do not think accoridng to the problem, think in reverse.
otherwise, whatever i get it will disappear.

interval DP

DP[i]][j]: minimum total points i can get for merging points between i and j
i   k  j
xxxxxxxx

dp[i][j] = min(dp[i][j], dp[i][k] + dp[k + 1][j] + sum(newA[i: j + 1])) for 0 <= i < j

answer:
dp[0][n - 1]

initial condition:
dp[i][i] = A[i]

time complexity:
o(n^3)

because the problem asks for circular, that means it is possible to start at point n-1 and then merge from around,
it is easier to increase the size of A to 2A so that I can connect them together.

prefix_sum

"""
class Solution:
    """
    @param A: An integer array
    @return: An integer
    """
    def stoneGame2(self, A):
        # write your code here
        if not A:
            return 0
        n_o = len(A) #original A's length
        newA = A + A #double it so it becomes circular
        n = len(newA)

        prefix_sum = self.cal_prefix_sum(newA)
        dp = [[sys.maxsize] * n for _ in range(n)]

        for i in range(n):
            dp[i][i] = 0

        for length in range(2, n + 1):
            for i in range(n - length + 1): #simpler but may result in mistakes
            # for i in range(n): #simpler way
                j = i + length - 1
                # if j > n - 1:  #simpler way
                #     continue
                for k in range(i, j):
                    # dp[i][j] = min(dp[i][j], dp[i][k] + dp[k + 1][j] + sum(newA[i: j + 1])) #without prefix sum
                    dp[i][j] = min(dp[i][j], dp[i][k] + dp[k + 1][j] + prefix_sum[j + 1] - prefix_sum[i])
        
        
        min_cost = sys.maxsize
        #iterate over starting point of the circular
        for i in range(n_o):
            min_cost = min(min_cost, dp[i][i + n_o - 1])
        return min_cost
        
        # return min([dp[i][i + n_o - 1] for i in range(n_o)]) #or u can use one-liner but it take extra space

    """
    calculate prefix_sum of ith *previous* numbers
    """
    def cal_prefix_sum(self, nums):
        n = len(nums)
        prefix_sum = [0] * (n + 1)
        for i in range(1, n + 1):
            prefix_sum[i] = prefix_sum[i - 1] + nums[i - 1]
            
        return prefix_sum