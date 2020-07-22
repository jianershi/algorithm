"""
428. Pow(x, n)
https://www.lintcode.com/problem/powx-n/description?_from=ladder&&fromId=152
"""
class Solution:
    """
    @param x {float}: the base number
    @param n {int}: the power number
    @return {float}: the result
    """
    def myPow(self, x, n):
        # write your code here
        if n == 0:
            return 1
 
        ans = 1
        positive = n > 0
        n = abs(n)
        while n > 0:
            if n & 1:
                ans *= x
            n >>= 1
            x *= x
        return ans if positive else 1/ans