"""
312. 牛牌
312. Bull Cards
https://www.lintcode.com/problem/bull-cards/description

knacksack problem
dp[i][j] select ith card to fill volume m 
= dp[i - 1][j] + (dp[i - 1][j - 1] if availab(i - 1))

dp[0][0] = 1

dp[n][m] answer
"""
class Solution:
    """
    @param n: the number 
    @param m: the number of cards in hand
    @return: the number of different types of cards
    """
    def bullCards(self, n, m):
        # Write your code here.
        MOD = 1000000007
        dp = [[0] * (m+1) for _ in range(n+1)]
        dp[0][0] = 1

        cards = [4] * n
        for i in range(1, n+1):
            dp[i][0] = 1
            for j in range(1, m+1):
                for count in range(5):
                    if j - count >= 0:
                        dp[i][j] = (dp[i][j] + dp[i - 1][j - count]) % MOD
                
        return dp[n][m] % MOD
        
s = Solution()
n = 4
m = 2
print(s.bullCards(n, m))