"""
582. Word Break II
https://www.lintcode.com/problem/word-break-ii/my-submissions
tle
"""
class Solution:
    """
    @param: s: A string
    @param: wordDict: A set of words.
    @return: All possible sentences.
    """
    def wordBreak(self, s, wordDict):
        # write your code here
        res = []
        self.dfs(s, 0, wordDict, [], res)
        return res
        
    def dfs(self, s, index, wordDict, path, res):
        n = len(s)
        if index == n:
            res.append(" ".join(path))
            return
        
        for i in range(index, n):
            if s[index: i + 1] not in wordDict:
                continue
            path.append(s[index:i + 1])
            self.dfs(s, i + 1, wordDict, path, res)
            path.pop()