"""
107. Word Break
https://www.lintcode.com/problem/word-break/description?_from=ladder&&fromId=160
DFS on word
"""
class Solution:
    """
    @param: s: A string
    @param: dict: A dictionary of words dict
    @return: A boolean
    """    
    def wordBreak(self, s, dict):
        return self.dfs(s, dict, 0, max([len(x) for x in dict]+[0]))

    def dfs(self, s, word_lists, index, max_word_len):
        n = len(s)
        if index == n:
            return True

        for i in range(index, n):
            if i - index + 1 > max_word_len:
                return False
            if s[index: i + 1] not in word_lists:
                continue
            if self.dfs(s, word_lists, i + 1, max_word_len):
                return True
        return False