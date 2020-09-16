"""
413. Reverse Integer
https://www.lintcode.com/problem/reverse-integer/description?_from=ladder&&fromId=37
"""
class Solution:
    """
    @param n: the integer to be reversed
    @return: the reversed integer
    """
    def reverseInteger(self, n):
        # write your code here
        
        a = str(abs(n))
        sign = n > 0
        res = int(a[::-1])
        if n > 0 and res <= 1<<31 - 1:
            return res
        if n < 0 and -res >= -1<<31:
            return -res
        return 0