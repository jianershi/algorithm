"""
402. Continuous Subarray Sum
https://www.lintcode.com/problem/continuous-subarray-sum/description
九章强化班C7
"""
import sys
class Solution:
    """
    @param: A: An integer array
    @return: A list of integers includes the index of the first number and the index of the last number
    """
    def continuousSubarraySum(self, A):
        # write your code here
        
        n = len(A)

        min_sum, min_sum_index = 0, -1
        res_index = -1, -1
        now_sum = 0
        max_sum = -sys.maxsize
        
        for i in range(n):
            now_sum += A[i]
            if now_sum - min_sum > max_sum:
                res_index = min_sum_index + 1, i
                max_sum = now_sum - min_sum
                
            if now_sum < min_sum:
                min_sum = now_sum
                min_sum_index = i
            
        return res_index