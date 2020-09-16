class Solution:
    """
    @param s: the maximum length of s is 1000
    @return: the longest palindromic subsequence's length
    """
    def longestPalindromeSubseq(self, s):
        # write your code here
        if not s:
            return 0
        start, end = 0, len(s) - 1
        memo =  [[None] * len(s) for _ in range(len(s))]
        return self.dfs(s, start, end, memo)

    def dfs(self, s, start, end, memo):
        # write your code here
        if memo[start][end] is not None:
            return memo[start][end]
        if start > end:
            memo[start][end] = 0
            return 0
        if start == end:
            memo[start][end] = 1
            return memo[start][end]
        if s[start] == s[end]:
            memo[start][end] = self.dfs(s, start + 1, end - 1, memo) + 2
        else:
            a = self.dfs(s, start + 1, end, memo)
            b = self.dfs(s, start, end - 1, memo)
            memo[start][end] = max(a, b)
        # print(max_length)
        return memo[start][end]
