"""
1350. Excel Sheet Column Title
https://www.lintcode.com/problem/excel-sheet-column-title/description
"""
class Solution:
    """
    @param n: a integer
    @return: return a string
    """
    def convertToTitle(self, n):
        # write your code here
        ret = ""
        while n:
            if n % 26 == 0:
                ret += 'Z'
                n -= 26
            else:
                ret += chr(ord('A') + n % 26 - 1)
            n //= 26
        return ret[::-1]