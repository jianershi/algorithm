"""
586. Sqrt(x) II
Implement double sqrt(double x) and x >= 0.

Compute and return the square root of x.

You do not care about the accuracy of the result, we will help you to output results.

binary search?
by result?

"""
class Solution:
    """
    @param x: a double
    @return: the square root of x
    """
    def sqrt(self, x):
        # write your code here
        if x >= 1:
            left, right = 0, x * 1.0
        else:
            left, right = x * 1.0, 1.0

        while right - left > 1e-10:
            mid = (left + right) / 2.0
            if mid * mid < x:
                left = mid
            else:
                right = mid

        return mid

s = Solution()
print(s.sqrt(3))
