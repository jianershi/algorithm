"""
512. Decode Ways
https://www.lintcode.com/problem/decode-ways/description
九章强化班

dp[i] = dp[i - 1] if last digit 1-9
        +dp[i - 2] if last 2 digits 1|0-9 or 2|0-6
dp[0] = 1

"""
class Solution:
    """
    @param s: a string,  encoded message
    @return: an integer, the number of ways decoding
    """
    def numDecodings(self, s):
        # write your code here
        if not s:
            return 0
        n = len(s)

        dp = [0] * (n + 1)

        dp[0] = 1

        for i in range(1, n + 1):
            if "1" <= s[i - 1] <= "9":
                dp[i] += dp[i - 1]
            if i > 1:
                if s[i - 2] == "1" and "0" <= s[i - 1] <= "9":
                    dp[i] += dp[i - 2]
                if s[i - 2] == "2" and "0" <= s[i - 1] <= "6":
                    dp[i] += dp[i - 2]

        return dp[n]
