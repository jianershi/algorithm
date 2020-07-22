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
        
        res = 0
        pos = n >= 0
        n = abs(n)
        while n > 0:
            res = 10 * res + n % 10
            n //= 10

        if pos and res <= 1<<31 -1:
            return res
        if not pos and -res >= -1<<31:
            return -res
        
        return 0