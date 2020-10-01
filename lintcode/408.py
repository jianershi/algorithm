"""
408. Add Binary
https://www.lintcode.com/problem/add-binary/description
"""
class Solution:
    """
    @param a: a number
    @param b: a number
    @return: the result
    """
    def addBinary(self, a, b):
        # write your code here
        res = ""
        i, j = len(a) - 1, len(b) - 1
        carry = 0
        while i >=0 or j >= 0:
            d = (int(a[i]) if i >= 0 else 0) + (int(b[j]) if j >= 0 else 0) + carry
            res += str(d % 2)
            carry = d // 2
            i -= 1
            j -= 1

        res += "1" if carry else ""
        return res[::-1]