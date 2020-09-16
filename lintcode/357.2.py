"""
357. Symmetrical Suffix
https://www.lintcode.com/problem/symmetrical-suffix/leaderboard?_from=contest&&fromId=103
"""
class Solution:
    """
    @param s: a string.
    @return: return the values of all the intervals.
    """
    def suffixQuery(self, s):
        # write your code here
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = 1
        
        count = 0
        # for r in range(n):
            # for l in range(r + 1):
        for length in range(1, n + 1):
            for l in range(n - length + 1):
                r = l + length - 1
                if s[l] != s[r]:
                    continue
                if l + 1 == r:
                    dp[l][r] = 2
                if l + 1 < r:
                    if dp[l + 1][r - 1] == r - l + 1 - 2:
                        dp[l][r] = dp[l + 1][r - 1] + 2
                    else:
                        dp[l][r] = dp[l + 1][r - 1] + 1
                        
                count += dp[l][r]
        return count