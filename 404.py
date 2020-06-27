"""
404. Subarray Sum II

https://www.lintcode.com/problem/subarray-sum-ii/description

九章强化班C7
"""
class Solution:
    """
    @param A: An integer array
    @param start: An integer
    @param end: An integer
    @return: the number of possible answer
    """
    def subarraySumII(self, A, start, end):
        # write your code here
        n = len(A)
        prefix_sum = [0] * (n + 1) #prefix_sum[j] = A[0... j - 1] #previous jth item
        l = r = 0
        count = 0
        for j in range(1, n + 1):
            prefix_sum[j] = prefix_sum[j - 1] + A[j - 1]
            """
            .....xxxoooooxxxxx..j
                    l    r
            """
            while l < j and prefix_sum[j] - prefix_sum[l] > end:
                l += 1

            while r < j and prefix_sum[j] - prefix_sum[r] >= start:
                r += 1

            count += r - l
        return count

