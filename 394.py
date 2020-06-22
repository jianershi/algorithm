"""
394. Coins in a Line
https://www.lintcode.com/problem/coins-in-a-line/description

f[i] with i coins left, weather i will win.
f[i] = f[i - 1] == False or f[i - 2] == False

f[0] = False
f[1] = f[2] = True

result: f[n]
"""
class Solution:
    """
    @param n: An integer
    @return: A boolean which equals to true if the first player will win
    """
    def firstWillWin(self, n):
        # write your code here
        if n == 0:
            return False
        if n < 3:
            return True

        dp = [False] * (n + 1)
        dp[0] = False
        dp[1] = dp[2] = True

        for i in range(3, n + 1):
            dp[i] = not dp[i - 1] or not dp[i - 2]

        return dp[n]
