"""
168. Burst Balloons
https://www.lintcode.com/problem/burst-balloons/description

dp[i][j] maximum coins collectable for breaking i + 1 to j - 1, i, j is unbreakable

dp[i][j] = max(dp[i][k] + dp[k][j] + nums[k] * nums[i] * nums[j] for k in range (i, j))

initial conditon
dp[i][i + 1] = 0

calculation process:
from smaller range to larger range

result
dp[0][n + 1]

time complexity:
choose all i and j O(n^2), then k inside O(n^3)
"""
class Solution:
    """
    @param nums: A list of integer
    @return: An integer, maximum coins
    """
    def maxCoins(self, nums):
        # write your code here
        if not nums:
            return 0
        nums = [1, *nums, 1]
        n = len(nums)
        dp = [[0] * n for _ in range(n)] #add two on the side

        print (nums)

        """
        注意：这一题必须先从length开始从小到大，然后再从开始点开始。
        原因是如果一开始从开始点开始，然后再从length开始增大的话就会变成0->1, 0->2, 0->3.
        这就不是我们想要的了。
        我们需要0->1, 1->2, 2->3这样子。遍历完了1的len以后再去开始2的。
        """
        for length in range(3, n + 1):
            """
            j = i + length - 1
            j < n
            i + length - 1 < n
            i < n + 1 - len
            """
            for i in range(n + 1 - length):
                j = i + length - 1
                for k in range(i + 1, j): #i+1, j-1
                    dp[i][j] = max(dp[i][j], dp[i][k] + dp[k][j] + nums[k] * nums[i] * nums[j])
        return dp[0][n - 1]
