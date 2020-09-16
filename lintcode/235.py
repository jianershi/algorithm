"""
235. Prime Factorization
https://www.lintcode.com/problem/prime-factorization/
"""
import math
class Solution:
    """
    @param num: An integer
    @return: an integer array
    """
    def primeFactorization(self, num):
        result = []
        up = math.sqrt(num)
        k = 2

        while k <= up and num > 1:
            while num % k == 0:
                result.append(k)
                num //= k
            k += 1

        if num > 1:
            result.append(num)

        return result
