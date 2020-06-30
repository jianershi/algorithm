"""
588. Partition Equal Subset Sum
https://www.lintcode.com/problem/partition-equal-subset-sum/description?_from=ladder&&fromId=160
九章高频题班C9 fb

thought process:

brute force: 
find all subset, then to see if there are two subsets with equal sum.
O(2^n) to find all combination

because it require the entire array to be partitioned into 2 subsets
if sum of all numbers are odd ->impossible
then sum // 2 for each partition.

-> problem becomes
pick from n numbers s that it fills to sum // 2 -> backsnack problem

dp[i][j], weahter i can fill exactly j with previous i items.

dp[i][j] = dp[i - 1][j] or dp[i - 1][j - nums[i - 1]]

initial condition: 
dp[i][0] = True

answer
dp[n][sum // 2]

2D array

"""
class Solution:
    """
    @param nums: a non-empty array only positive integers
    @return: true if can partition or false
    """
    def canPartition(self, nums):
        # write your code here
        if not nums:
            return False

        if sum(nums) % 2 != 0:
            return False

        n = len(nums)
        sums = sum(nums) // 2
        
        dp = [[False] * (sums + 1) for _ in range(2)]

        now, old = 0, 0
        # for i in range(n + 1):
        #     dp[i][0] = True
        dp[now][0] = True

        for i in range(1, n + 1):
            old = now
            now = 1 - now
            for j in range(1, sums + 1):
                dp[now][j] = dp[old][j]
                if j >= nums[i -  1]:
                    dp[now][j] = dp[now][j] or dp[old][j - nums[i - 1]]

        return dp[now][sums]