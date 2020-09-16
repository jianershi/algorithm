"""
676. Decode Ways II
https://www.lintcode.com/problem/decode-ways-ii/description
九章强化班

dp[i] = dp[i - 1]
        + dp[i - 2]

dp[0] = 1 empty string, 1 way to decode
because dp[1] = 1-9 + dp[0]. easier to calculate
"""
class Solution:
    """
    @param s: a message being encoded
    @return: an integer
    """
    def numDecodings(self, s):
        # write your code here
        if not s:
            return 0
        n = len(s)

        MOD = 1000000007

        dp = [0] * (n + 1)

        dp[0] = 1

        for i in range(1, n + 1):
            dp[i] = dp[i - 1] * self.last_digit_weight(s[i - 1])
            if i > 1:
                dp[i] += dp[i - 2] * self.last_two_digits_weight(s[i - 2], s[i - 1])

            dp[i] %= MOD

        return dp[n]

    def last_digit_weight(self, last_digit):
        if last_digit == "0":
            return 0
        if "1" <= last_digit <= "9":
            return 1
        if last_digit == "*":
            return 9

    def last_two_digits_weight(self, second_last_digit, last_digit):
        if second_last_digit == "0":
            return 0
        if second_last_digit == "1":
            if "0" <= last_digit <= "9":
                return 1
            if last_digit == "*":
                return 9
        if second_last_digit == "2":
            if "0" <= last_digit <= "6":
                return 1
            if "7" <= last_digit <= "9":
                return 0
            if last_digit == "*":
                return 6
        if "3" <= second_last_digit <= "9":
            return 0
        if second_last_digit == "*":
            if "0" <= last_digit <= "6":
                return 2
            if "7" <= last_digit <= "9":
                return 1
            if last_digit == "*":
                return 15
