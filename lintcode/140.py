"""
140. Fast Power
calculate a^n % b
"""
class Solution:
    """
    @param a: A 32bit integer
    @param b: A 32bit integer
    @param n: A 32bit integer
    @return: An integer
    """
    def fastPower(self, a, b, n):
        # write your code here
        if n == 0:
            return 1 % b
        if n == 1:
            return a % b

        ans = 1
        base = a
        power = n

        while power > 0:
            if power & 1:
                ans *= base % b
            base *= base % b
            power >>= 1

        return ans % b
