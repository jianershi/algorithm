"""
1139. the kth subarray
https://www.lintcode.com/problem/the-kth-subarray/description?_from=ladder&&fromId=160
"""
class Solution:
    """
    @param a: an array
    @param k: the kth
    @return: return the kth subarray
    """
    def thekthSubarray(self, a, k):
        # wrrite your code here
        start, end = 1, sum(a)
        while start + 1 < end:
            mid = start + (end - start) // 2
            count = self.count_subarray(a, mid)
            if count > k:
                end = mid
            if count < k:
                start = mid
            if count == k:
                end = mid
        if self.count_subarray(a, start) >= k:
            return start
        if self.count_subarray(a, end) >= k:
            return end

    def count_subarray(self, nums, target):
        n = len(nums)
        left = 0
        cur_sum = 0
        count = 0
        for right in range(n):
            cur_sum += nums[right]
            while left < right and cur_sum > target:
                left += 1
                cur_sum -= nums[left - 1]
            if cur_sum <= target:
                count += right - left + 1
        return count


s = Solution()
a=[17]
k=1
print(s.thekthSubarray(a, k))
