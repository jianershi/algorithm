"""
395. Coins in a Line II

https://www.lintcode.com/problem/coins-in-a-line-ii/description

dp[i]: maximum total advantage over opponennt when there are i - n coins left to choose

the definition of dp can also be represented this way:
now: Sx = X - Y
next: Sy = Y - X
X, Y being the sum of coins one can choose from i to n so that it results in max advantage Sx, Sy

now choose m
------------------
now  |    m
next |    X', Y'
------------------
by definition:
dp[i] = m + X' - Y' maximum advantage over opponent from *current* step onwards
dp[i + 1] = Y' - X' maximum advantage over opponent from *current* step onwards
==> dp[i] = m - dp[i + 1]

dp[i] = max(values[i] - dp[i + 1], values[i] + values[i + 1] - dp[i + 2])

intial condition
dp[n] = 0 no coin left

calculation direction:
n -> 0

result:
f[0] >= 0

"""
class Solution:
    """
    @param values: a vector of integers
    @return: a boolean which equals to true if the first player will win
    """
    def firstWillWin(self, values):
        # write your code here
        if not values:
            return 0
        n = len(values)

        dp = [0] * (n + 1)

        dp[n] = 0

        for i in range(n - 1, -1, -1):
            #dp[n - 1] = values[n - 1] - dp[n]
            dp[i] = values[i] - dp[i + 1]
            if i < n - 1:
                dp[i] = max(dp[i], values[i] + values[i + 1] - dp[i + 2])

        return dp[0] >= 0
