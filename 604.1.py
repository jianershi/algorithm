class Solution:
    """
    @param nums: a list of integers.
    @param k: length of window.
    @return: the sum of the element inside the window at each moving.
    """
    def winSum(self, nums, k):
        # write your code here
        """
        如果纯暴力2个循环，O(N*k)。
        优化的话直接用滑动窗口，每次只往右滑1个位置，固定+1个值，-1个值。
        第一次建立窗口花O(k),然后之后每次滑动花固定的2*O(1)时间。总共花O(k+n)的时间
        """
        result = []
        if not nums:
            return result
        sum = 0
        for i in range(k):
            if i < len(nums):
                sum += nums[i]
        result.append(sum)
        for i in range(k, len(nums)):
            sum += nums[i] - nums[i - k]
            result.append(sum)

        return result
