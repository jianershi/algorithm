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
        if n == 0:
            return 1 % b

        temp = self.fastPower(a, b, n // 2)
        total = (temp % b * temp % b) % b

        if n % 2 == 1:
            total = (total % b * a % b) % b

        return total
