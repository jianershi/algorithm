"""
1. dp
state - f[i] length of LIS including i
transfer function:
f[i] = max (j in 0 ~ i -1 f[j]) for A[i] > A[j]  +1
initial condition
f[i] = 1
answer:
max(f)
direction: from left to right

"""
class Solution:
    """
    @param nums: An integer array
    @return: The length of LIS (longest increasing subsequence)
    """
    def longestIncreasingSubsequence(self, nums):
        # write your code here
        if not nums:
            return 0
        n = len(nums)
        f = [1] * n
        prev = [-1] * n
        
        for i in range(0, n):
            for j in range(0, i):
                if nums[i] > nums[j]:
                    # f[i] = max(f[i], f[j] + 1)
                    if f[i] < f[j] + 1:
                        f[i] = f[j] + 1
                        prev[i] = j
        lis_max_length = max(f)
        
                
        last = 0
        for i in range(len(f)):
            if f[i] > f[last]:
                last = i
        path = [nums[last]]
        while prev[last] != -1:
            last = prev[last]
            path.append(nums[last])
        
        print(path[::-1])
        
        return lis_max_length