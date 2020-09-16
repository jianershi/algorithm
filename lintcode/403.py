"""
403. Continuous Subarray Sum II
https://www.lintcode.com/problem/continuous-subarray-sum-ii/description

Similar to 402, 402 is a continous subarray sum, but this one is rotating array subarray sum.
-> find max sub in a non rotating array: S1
then find min (not empty subset) S2
overall sum S
fight! S1 vs S - S2

"""
class Solution:
    """
    @param: A: An integer array
    @return: A list of integers includes the index of the first number and the index of the last number
    """
    def continuousSubarraySumII(self, A):
        # write your code here
        if not A:
            return -1, -1

        n = len(A)
        now_sum = 0
        
        max_subarray_sum = -sys.maxsize
        max_subarray_index = None, None
        min_sum, min_sum_index = 0, -1

        min_subarray_sum = sys.maxsize
        min_subarray_index = None, None
        max_sum, max_sum_index = 0, -1

        for i in range(n):
            now_sum += A[i]
            if now_sum - min_sum > max_subarray_sum:
                max_subarray_sum = now_sum - min_sum
                max_subarray_index = min_sum_index + 1, i

            if now_sum - max_sum < min_subarray_sum:
                min_subarray_sum = now_sum - max_sum
                min_subarray_index = max_sum_index + 1, i

            if now_sum < min_sum:
                min_sum = now_sum
                min_sum_index = i

            if now_sum > max_sum:
                max_sum = now_sum
                max_sum_index = i

        if max_subarray_sum < now_sum - min_subarray_sum and min_subarray_index[1] - min_subarray_index[0] != len(A) - 1:
            return (min_subarray_index[1] + 1) % n, (min_subarray_index[0] - 1) % n
        return max_subarray_index

