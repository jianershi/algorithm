"""
119. Edit Distance
https://www.lintcode.com/problem/edit-distance/description?_from=ladder&&fromId=106
九章算法强化班。经典DP题

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
        if not word1 and not word2:
            return 0

        m = len(word1)
        n = len(word2)

        dp = [[sys.maxsize] * (n + 1) for _ in range(m + 1)]

        for i in range(m + 1):
            for j in range(n + 1):
                if i == 0:
                    dp[0][j] = j
                    continue
                if j == 0:
                    dp[i][0] = i
                    continue
                
                dp[i][j] = min( dp[i][j - 1] + 1,       #add
                                dp[i - 1][j] + 1,   #del
                                dp[i - 1][j - 1] + 1    #replace
                            )
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = min(dp[i][j], dp[i - 1][j - 1])

        return dp[m][n]