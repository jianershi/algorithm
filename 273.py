"""
273. Test Strategy
https://www.lintcode.com/problem/test-strategy/description?_from=contest&&fromId=95
"""
class Solution:
    """
    @param p: The time you choose to do part of the problem.
    @param part: The points you choose to do part of the problem.
    @param f: The time you choose to do the whole problem.
    @param full: The points you choose to do the whole problem.
    @return: Return the maximum number of points you can get.
    """
    def exam(self, p, part, f, full):
        # write your code here
        if not p or not part or not f or not full:
            return 0
        timelimit = 120
        n = len(p)
        dp = [[0] * (timelimit + 1) for _ in range(n + 1)]
        
        for i in range(1, n + 1):
            for j in range(1, timelimit + 1):
                dp[i][j] = dp[i - 1][j]
                if j >= p[i - 1]:
                    dp[i][j] = max(dp[i][j], dp[i - 1][j - p[i - 1]] + part[i - 1])
                if j >= f[i - 1]:
                    dp[i][j] = max(dp[i][j], dp[i - 1][j - f[i - 1]] + full[i - 1])
        
        return max(dp[n])