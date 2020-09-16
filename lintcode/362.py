"""
362. Sliding Window Maximum
https://www.lintcode.com/problem/sliding-window-maximum/description?_from=ladder&&fromId=106
单调栈->单调双端队列
九章强化班
"""
from collections import deque
class Solution:
    """
    @param nums: A list of integers.
    @param k: An integer
    @return: The maximum number inside the window at each moving.
    """
    def maxSlidingWindow(self, nums, k):
        # write your code here
        result = []
        queue = deque()
        for i, num in enumerate(nums):
            while queue and nums[queue[-1]] < num:
                queue.pop()
            queue.append(i)
            if i >= k - 1:
                result.append(nums[queue[0]])
            if queue[0] == i - k + 1:
                queue.popleft()
        return result
