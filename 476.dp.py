import sys
class Solution:
    """
    @param A: An integer array
    @return: An integer
    """
    def stoneGame(self, A):
        if not A:
            return 0
        dp = [[sys.maxsize] * len(A) for _ in range(len(A))]
        for i in range(len(A)):
            dp[i][i] = 0
        prefix_sum = self.calculate_prefix_sum(A)
        for length in range(1, len(A) + 1):
            for start in range(0, len(A) - length + 1):
                end = start + length - 1
                # curr_range_sum = sum(A[start: end + 1])
                if start == 0:
                    curr_range_sum = prefix_sum[end]
                else:
                    curr_range_sum = prefix_sum[end] - prefix_sum[start - 1]
                for k in range(start, end):
                    dp[start][end] = min(dp[start][end], dp[start][k] + dp[k + 1][end] + curr_range_sum)
        # print (dp[0][len(A) - 1])
        return (dp[0][len(A) - 1])

    def calculate_prefix_sum(self, nums):
        if not nums:
            return None
        prefix_sum = [0] * len(nums)
        prefix_sum[0] = nums[0]
        for i in range(1, len(nums)):
            prefix_sum[i] = (prefix_sum[i - 1] + nums[i])
        return prefix_sum
A = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

s = Solution()
print(s.stoneGame(A))
