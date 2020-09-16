"""
265. Maximum Non-Negative Subarray
https://www.lintcode.com/problem/maximum-non-negative-subarray/description?_from=contest&&fromId=93
"""
import sys
class Solution:
    """
    @param A: an integer array
    @return: return maxium contiguous non-negative subarray sum
    """
    def maxNonNegativeSubArray(self, A):
        # write your code here
        if not A:
            return 0
        n = len(A)
        
        now_sum = 0
        max_sum = -sys.maxsize

        all_negative = True
        for i in range(n):
            if A[i] >= 0:
                all_negative = False

            if i != n - 1 and A[i] >= 0:
                now_sum += A[i]
                continue
            if i == n - 1 and A[i] >= 0:
                now_sum += A[i]

            max_sum = max(max_sum, now_sum)
            now_sum = 0

        return max_sum if not all_negative else - 1

s = Solution()
A = [0]
print(s.maxNonNegativeSubArray(A))