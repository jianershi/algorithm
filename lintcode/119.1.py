"""
119. Edit Distance
https://www.lintcode.com/problem/edit-distance/description?_from=ladder&&fromId=106
九章算法强化班。经典DP题 (第二次写)

didn't sepcifiy direction/sequence, i can specify from left to right.

last step:
I can either add a char, delete or replace a character from word1->word2:
e.x. mart -> karma

add: a is added dp[i][j] = dp[i][j - 1] + 1
delete: t is removed: dp[i][j] = dp[i - 1][j] + 1
replace: t->a: dp[i][j] = dp[i - 1][j - 1] + 1
match: e.x. marta -> karma: dp[i][j] = dp[i - 1][j - 1]
dp[i][j]: minimum number of steps to change first i char from word1 to first j chars from word2
min of all 4 steps. any of those 4 steps make the problem scale smaller ->dp

answer:
dp[m][n]

initial condition:
dp[0][j] = j from empty string to string, add j steps
dp[i][0] = i from non-empty string to empty string, remove j steps

"""
class Solution:
    """
    @param word1: A string
    @param word2: A string
    @return: The minimum number of steps.
    """
    def minDistance(self, word1, word2):
        # write your code here
        n = len(word1)
        m = len(word2)
        dp = [[sys.maxsize] * (m + 1) for _ in range(n + 1)]
        
        for i in range(n + 1):
            dp[i][0] = i
        for j in range(m + 1):
            dp[0][j] = j
        
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = min(dp[i][j], dp[i-1][j-1])
                dp[i][j] = min(dp[i][j],
                            dp[i - 1][j] + 1,
                            dp[i][j - 1] + 1,
                            dp[i - 1][j - 1] + 1
                            )
        return dp[n][m]