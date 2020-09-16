"""
107. Word Break
https://www.lintcode.com/problem/word-break/description?_from=ladder&&fromId=160
Memoization
"""
class Solution:
    """
    @param: s: A string
    @param: dict: A dictionary of words dict
    @return: A boolean
    """
    def wordBreak(self, s, dict):
        # write your code here
        if dict:
            max_dict_word_length = max([len(x) for x in dict])
        else:
            max_dict_word_length = 0
            
        return self.can_break(s, 0, dict, max_dict_word_length, {})
    
    def can_break(self, s, i, dict, max_dict_word_length, memo):
        if i in memo:
            return memo[i]
        if len(s) == i:
            return True

        for index in range(i, len(s)):
            if index - i > max_dict_word_length:
                break
            if s[i:index + 1] not in dict:
                continue
            if self.can_break(s, index + 1, dict, max_dict_word_length, memo):
                memo[i] = True
                return memo[i]
        return False
  