"""
430. Scramble String
https://www.lintcode.com/problem/scramble-string/description?_from=ladder&&fromId=106

DP.
Same thought as DFS.But using DP

DP[n][i][j] : for length n substring starting from position i in s1 and staring j in s2. are they scrambled?

dp[n][i][j] = dp[k][i][j] and dp[n - k][i + k][j + k] \
            or dp[k][i][j + n - k] and dp[n - k][i + k][j]
            for i < k < j

initial condition: any length 1 just have to compare characters
dp[1][i][j] = (s1[i] == s2[j])

answer:
dp[n][0][0]

calculation direction:
length small->big, so length must be the outmost layer of for loop

time complexity
o(n^3)
space complexity
o(n^3)

"""
class Solution:
    """
    @param s1: A string
    @param s2: Another string
    @return: whether s2 is a scrambled string of s1
    """
    def isScramble(self, s1, s2):
        if not s1 or not s2:
            return False
        size = len(s1)
        if size != len(s2):
            return False
        if sorted(s1) != sorted(s2):
            return False

        dp = [[[False] * size for _ in range(size)] for _ in range(size + 1)]

        for i in range(size):
            for j in range(size):
                dp[1][i][j] = (s1[i] == s2[j])

        """
        这里是一段长度为n的区间，判断长度为n的区间，且s1中开始点为i， s2中开始点为j的两端长度为n的区间是否为scramble.
        n 是长度，所以可以是1-n
        i 是起始点

            total size of s1/s2
        ----------------------------
        xxxxxxxxxxxxxxxx|xxxxxxxxxxx
                        |<--- n  --->
                        i
        so i can have from 0 to size - n
        same for j
        k 是左半边的分割，所以长度至少为1，最长也是n - 1
        """
        for n in range(2, size + 1): #1-n
            for i in range(size - n + 1): #i .... i + len - 1.
                for j in range(size - n + 1):
                    for k in range(1, n): # 1 - n - 1
                        if dp[k][i][j] and dp[n - k][i + k][j + k] \
                                or dp[k][i][j + n - k] and dp[n - k][i + k][j]:
                            dp[n][i][j] = True
                            break

        return dp[size][0][0]
