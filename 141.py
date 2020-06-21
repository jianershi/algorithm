"""
141. Sqrt(x)
https://www.lintcode.com/problem/sqrtx/description?_from=ladder&&fromId=106
"""
class Solution:
    """
    @param x: An integer
    @return: The sqrt of x
    """
    def sqrt(self, x):
        # write your code here
        start, end = 0, x

        while start + 1 < end:
            mid = (start + end) // 2
            if mid * mid < x:
                start = mid
            else:
                end = mid
        if end * end <= x:
            return end
        return start
