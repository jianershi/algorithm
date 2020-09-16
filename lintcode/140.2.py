"""
140. Fast Power
calculate a^n % b
2nd time
"""
class Solution:
    """
    @param a: A 32bit integer
    @param b: A 32bit integer
    @param n: A 32bit integer
    @return: An integer
    """
    def fastPower(self, a, b, n):
        ans = 1
        base = a
        while n > 0:
            if n & 1:
                ans = (ans % b * base % b) % b
            base = (base % b * base % b) % b
            n >>= 1
        return ans % b
