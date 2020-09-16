"""
77. Longest Common Subsequence
https://www.lintcode.com/problem/longest-common-subsequence/description?_from=ladder&&fromId=106
九章强化班。 DP 高频题

dp: longest common subsequence from frist i character of A and first j character of B

last step:
A's last character != B's last character: ditch a's last character or b's last character and match rest
dp[i][j] = max(dp[i - 1]dp[j], dp[i][j - 1]

A's last character match B's last character: then those 2 character have to link together.
because if they don't link together, there is going to be crosses between the two strings, which does
not match the definition of subsequence

A:a b
   x
B:b a

not allowed.

so:
dp[i][j] = max(dp[i-1][j-1] + 1)

initalization:
dp[0][j] = 0 longest subsequence from empty string to a non-empty string is always 0
dp[i][0] = 0

answer : dp[m][n]

calculation direction:from front to back

"""
class Action:
    MATCH = 2
    MOVE_A = 1
    MOVE_B = 0
class Solution:
    """
    @param A: A string
    @param B: A string
    @return: The length of longest common subsequence of A and B
    """
    def longestCommonSubsequence(self, A, B):
        # write your code here
        if not A or not B:
            return 0
        m = len(A)
        n = len(B)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        history = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
                if dp[i][j] == dp[i - 1][j]:
                    history[i][j] = Action.MOVE_A
                else:
                    history[i][j] = Action.MOVE_B
                if A[i - 1] == B[j - 1]:
                    dp[i][j] = max(dp[i][j], dp[i - 1][j - 1] + 1)
                    if dp[i][j] == dp[i - 1][j - 1] + 1:
                        history[i][j] = Action.MATCH

        #printing
        LCS = ""
        i, j = m, n
        while i > 0:
            while j > 0:
                if history[i][j] == Action.MOVE_A:
                    i -= 1
                elif history[i][j] == Action.MOVE_B:
                    j -= 1
                else:
                    LCS += A[i - 1]
                    i -= 1
                    j -= 1
        
        LCS = LCS[::-1]
        
        print (LCS)

        return dp[m][n]