"""
107. Word Break
https://www.lintcode.com/problem/word-break/description?_from=ladder&&fromId=160
DFS on dictionary
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
        if (index == len(s)):
            return True
        
        for word in wordSet:
            if not s[index:].startswith(word):
                continue
            if self.dfs(index + len(word), s, wordSet):
                return True
        
        return False