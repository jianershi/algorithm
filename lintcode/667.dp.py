"""
dp[i][j] max length of susbstrings between range i and j
if s[i] == s[j], then dp[i][j] = dp[i + 1][j - 1] + 2
else: max(dp[i - 1][j], dp[i][j - 1])

inittalization
dp[i][j] = 1

算法方向
range从小到大。

https://www.youtube.com/watch?v=_nCsPn7_OgI

"""
class Solution:
    """
    @param s: the maximum length of s is 1000
    @return: the longest palindromic subsequence's length
    """
    def longestPalindromeSubseq(self, s):
        # write your code here
        if not s:
            return 0
        dp =  [[0] * len(s) for _ in range(len(s))]
        for length in range(len(s)):
            for i in range (len(s) - length):
                j = i + length
                if i == j:
                    dp[i][j] = 1
                    continue
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
        return dp[0][len(s) - 1]

s = Solution()
# s.longestPalindromeSubseq("asdasdajjdkajwiejladjkahsdjhawiueauwhdjashdjancnkjsahduiawudhajsnhsjahjdhawuahdjshjnzanjcnhjdashuawhdjaksndjkahduwhwauhdai")
print(s.longestPalindromeSubseq("abkcbcka"))
