"""
761. Smallest Subset
https://www.lintcode.com/problem/smallest-subset/description

first sort, then calculate prefix sum.
"""
class Solution:
    """
    @param arr:  an array of non-negative integers
    @return: minimum number of elements
    """
    def minElements(self, arr):
        # write your code here
        if not arr:
            return -1

        arr = sorted(arr)
        n = len(arr)

        prefix_sum = [0] * (n + 1)
        for i in range(1, n + 1):
            prefix_sum[i] = prefix_sum[i - 1] + arr[i - 1]

        now_sum = 0
        count = 0
        for i in range(n - 1, -1, -1):
            now_sum += arr[i]
            count += 1
            if now_sum > prefix_sum[i]:
                return count

        return -1 