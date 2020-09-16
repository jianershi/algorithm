"""
29. Interleaving String
https://www.lintcode.com/problem/interleaving-string/description?_from=ladder&&fromId=106
九章强化班

dp: whether the first k chars of s3 is formed by first i chars of s1 and j chars of s2
last step: since X is made up with A and B, then the last char of X must be comprised of either A's last char or B's last char
dp[k][i][j] = dp[k][i - 1][j] and X[k - 1] == A[i - 1] or dp[k][i][j - 1] and X[k - 1] == B[j - 1]
in dp, we can have 1 less degree by noticing k = i + j at all times.
dp[i][j] = dp[i - 1][j] and X[i + j - 1] == A[i - 1] or dp[i][j - 1] and X[i + j - 1] == B[j - 1]

initial condition:
dp[0][0] = True empty string and empty string can makeup an empty string

answer:
dp[m][n]

"""
class Solution:
    """
    @param s1: A string
    @param s2: A string
    @param s3: A string
    @return: Determine whether s3 is formed by interleaving of s1 and s2
    """
    def isInterleave(self, s1, s2, s3):
        # write your code here
        m = len(s1)
        n = len(s2)

        dp = [[False] * (n + 1) for _ in range(m + 1)]
        
        for i in range(m + 1):
            for j in range(n + 1):
                if i == 0 and j == 0:
                    dp[0][0] = True
                    continue
                
                dp[i][j] = dp[i - 1][j] and s3[i + j - 1] == s1[i - 1] \
                        or dp[i][j - 1] and s3[i + j - 1] == s2[j - 1]

        return dp[m][n]