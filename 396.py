"""
396. Coins in a Line III
https://www.lintcode.com/problem/coins-in-a-line-iii/description
因为在无论第几步，在任何一人个人面对这个的时候都是一个完整的区间->区间形动态规划。

dp[i][j]: maximum amount of advantage can get when there are i-j coins left
dp[i][j] = max(values[i] - dp[i + 1][j], values[j] - dp[i][j - 1])

result:
dp[0][n - 1] >= 0

calculation direction: inside -> outside

initial condition:
dp[i][i] = values[i]

"""

class Solution:
    """
    @param values: a vector of integers
    @return: a boolean which equals to true if the first player will win
    """
    def firstWillWin(self, values):
        # write your code here
        if not values:
            return False

        n = len(values)

        dp = [[0] * n for _ in range(n)]

        #initial condition, 1 left, then whoever grabs it, can grab all
        for i in range(n):
            dp[i][i] = values[i]

        for lenth in range(2, n + 1):
            """
            j = i + len - 1
            i + len - 1 < n:
            i < n - len + 1
            """
            for i in range(n - lenth + 1):
                j = i + lenth - 1
                dp[i][j] = max(values[i] - dp[i + 1][j], values[j] - dp[i][j - 1])

            """
            不需要单独考虑i+1 == j的情况，也就是只有2个数的情况，因为dp继续通用：
            dp[0][1] = max(values[0]- dp[1][1], values[1] - dp[0][0])
                     = max(values[0] - values[1], values[1] - values[0])
            """
        return dp[0][n - 1] >= 0
