"""
107. Word Break
https://www.lintcode.com/problem/word-break/description?_from=ladder&&fromId=160
DFS 2^n
"""
class Solution:
    """
    @param s: A string
    @param wordSet: A dictionary of words dict
    @return: A boolean
    """
    def wordBreak(self, s, wordSet):
        # write your code here
        return self.dfs(0, s, wordSet)
        
    def dfs(self, index, s, wordSet):
        n = len(s)
        if (index == len(s)):
            return True
        
        for i in range(index, n):
            if s[index:i+1] not in wordSet:
                continue
            if self.dfs(i+1, s, wordSet):
                return True
        
        return False