"""
107. Word Break
https://www.lintcode.com/problem/word-break/description?_from=ladder&&fromId=160
DFS on dictionary
"""
class Solution:
    """
    @param: s: A string
    @param: dict: A dictionary of words dict
    @return: A boolean
    """    
    def wordBreak(self, s, dict):
        return self.dfs(s, dict, 0)

    def dfs(self, s, word_lists, index):
        if index == len(s):
            return True
        if index > len(s):
            return False

        for word in word_lists:
            if s[index:].startswith(word):
                if self.dfs(s, word_lists, index + len(word)):
                    return True
                    
        return False