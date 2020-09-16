"""
65. Median of two Sorted Arrays
https://www.lintcode.com/problem/median-of-two-sorted-arrays/description
2nd try
"""
import sys
class Solution:
    """
    @param: A: An integer array
    @param: B: An integer array
    @return: a double whose format is *.5 or *.0
    """
    def findMedianSortedArrays(self, A, B):
        a = len(A)
        b = len(B)

        if (a + b) % 2 == 1:
            return self.find_kth(A, 0, a - 1, B, 0, b - 1, (a + b) // 2 + 1)
        else:
            return (self.find_kth(A, 0, a - 1, B, 0, b - 1, (a + b) // 2) + self.find_kth(A, 0, a - 1, B, 0, b - 1, (a + b) // 2 + 1)) / 2.0

    def find_kth(self, A, a_start, a_end, B, b_start, b_end, kth):
        if a_start > a_end:
            return B[b_start + kth - 1]
        if b_start > b_end:
            return A[a_start + kth - 1]
        if kth == 1:
            return min(A[a_start], B[b_start])

        mid = kth // 2

        a_mid = A[a_start + mid - 1] if a_start + mid - 1 <= a_end else sys.maxsize
        b_mid = B[b_start + mid - 1] if b_start + mid - 1 <= b_end else sys.maxsize

        if a_mid < b_mid:
            return self.find_kth(A, a_start + mid, a_end, B, b_start, b_end, kth - (mid))
        return self.find_kth(A, a_start, a_end, B, b_start + mid, b_end, kth - (mid))

s = Solution()
A = [1,3,9,10]

B = [1,4,6,6,10,11]
print(s.findMedianSortedArrays(A, B))
