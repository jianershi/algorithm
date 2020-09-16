"""
1844. subarray sum equals k II


thought process:

since this problem is to ask for subarray sum.
it is intuitive to think about prefix sum.
pre-calculate prefix sum.
then for any continuous subarray. need o(1) to find sum.

however, need to iterate over starting point end ending point.
that alone can take o(n^2). wondering if there are faster ways to do it.


"""
class Solution:
    """
    @param nums: a list of integer
    @param k: an integer
    @return: return an integer, denote the minimum length of continuous subarrays whose sum equals to k
    """
    def subarraySumEqualsKII(self, nums, k):
        # write your code here
        prefix_sum_index = {0:-1}
        sum = 0
        min_length = sys.maxsize
        for j in range(len(nums)):
            sum += nums[j]
            if sum - k  in prefix_sum_index:
                min_length = min(min_length, j - prefix_sum_index[sum - k])

            prefix_sum_index[sum] = j

        return min_length if min_length != sys.maxsize else -1
