"""
402. Continuous Subarray Sum
https://www.lintcode.com/problem/continuous-subarray-sum/description
九章强化班C7

这边难得是初始条件：
首先是前缀和问题。所以min_sum是0就可以了。 这样前缀和 max - 0 = max也没问题。
然后就是min_index得是-1
考虑只有一个元素
[-3]
这个时候i在0，我们要返回[0, 0]
本来的前缀和是

.....i....j = prefix[j] - prefix[i] = sum (A[i + 1] ..... A[j])。所以只要一开始是-1的话-1 + 1 = 0也没问题
即使只有一个元素，即使第一个是负的。只要min_sum 是0， max_subarray_sum = - sys.maxsize也能更新。并且更新的位置也对。 min_index(-1) + 1 = 0
这样就没问题了。
"""
import sys
class Solution:
    """
    @param: A: An integer array
    @return: A list of integers includes the index of the first number and the index of the last number
    """
    def continuousSubarraySum(self, A):
        n = len(A)

        max_subarray_sum = -sys.maxsize
        max_subarray_index = None, None
        min_sum, min_index = 0, -1

        now_sum = 0

        for i in range(n):
            now_sum += A[i]
            if now_sum - min_sum > max_subarray_sum:
                max_subarray_sum = now_sum - min_sum
                max_subarray_index = min_index + 1, i

            if now_sum < min_sum:
                min_sum = now_sum
                min_index = i

        return max_subarray_index