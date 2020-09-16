"""
414. Divide Two Integers
https://www.lintcode.com/problem/divide-two-integers/description?_from=ladder&&fromId=106
"""
import sys
class Solution:
    """
    @param dividend: the dividend
    @param divisor: the divisor
    @return: the result
    """
    def divide(self, dividend, divisor):
        # write your code here
        a = abs(dividend)
        b = abs(divisor)

        result = 0

        while a >= b:
            tmp = b
            count = 1
            while a >= tmp:
                a -= tmp
                result += count
                tmp <<= 1
                count <<= 1

        if (dividend > 0) ^ (divisor > 0):
            if result < -2**31 - 1:
                return -2147483648
            return -result

        if result >= 2**31:
            return 2147483647
        return result
