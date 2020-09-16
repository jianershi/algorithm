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
 
        ans = myPow (x, n // 2)
        if n % 2 == 0:
            return ans * ans
        return ans * ans * x