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
            ret += chr(ord('A') + (n - 1) % 26)
            n = (n - (n - 1) % 26 - 1) // 26
        return ret[::-1]