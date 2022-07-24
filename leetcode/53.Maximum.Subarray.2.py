"""
53. Maximum Subarray
prefix sum

....i....j
     ^   ^
sum = A[j] - A[i]

cur_sum = A[0] + ... + A[j]
min_sum = ending in index j, the least sum ever occred
        = min(min_sum, cur_sum)
max_sum = ending in idnex j, the largest sum ever occcured:
        = max(max_sum, cur_sum - min_sum)

o(n)
"""
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur_sum = 0
        max_sum = -sys.maxsize
        min_sum = 0
        
        for num in nums:
            cur_sum += num
            max_sum = max(max_sum, cur_sum - min_sum)
            min_sum = min(cur_sum, min_sum)
            
        return max_sum