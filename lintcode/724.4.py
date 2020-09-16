"""
724. Minimum Partition
https://www.lintcode.com/problem/minimum-partition/description

01背包
算法班2020 C27 01背包变形

第二种dp定义
dp[i][j]: considering previous i items, whether it is possible to fill sum j

dp[i][j] = dp[i - 1][j] or dp[i - 1][j - nums[i - 1]] if j >= nums[i - 1]

dp[0][0] = True
dp[i][0] = False

answer
max(dp[n])

1d array TLE
"""
class Solution:
    """
    @param nums: the given array
    @return: the minimum difference between their sums 
    """
    def findMin(self, nums):
        # write your code here
        if not nums:
            return 0

        n = len(nums)
        total_sum = sum(nums)
        target = total_sum // 2

        print (n, total_sum, target)
        dp = [False] * (target + 1)
        dp[0] = True

        for i in range(1, n + 1):
            for j in range(target, nums[i - 1] -1, -1):
                dp[j] |= dp[j - nums[i - 1]]

        for j in range(target, -1, -1):
            if dp[j]:
                return total_sum - 2 * j


        

s = Solution()
nums =[1,21]
print(s.findMin(nums))