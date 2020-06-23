"""
107. Word Break
https://www.lintcode.com/problem/word-break/description?_from=ladder&&fromId=160
DP
"""
class Solution:
    """
    @param: s: A string
    @param: dict: A dictionary of words dict
    @return: A boolean
    """
    """
    state: f[i] 代表到i位为止的字符是否能被连续切分
    转换方程: f[i] = OR(for j in 0, len(s)) f[j] and s[i - j] in dict
    初始值: f[0] True
    边界条件i - j >= 0
    答案: f[len(s)]
    计算顺序：从左往右
    """
    
    def wordBreak(self, s, dict):
        if not s:
            return True
        if not dict:
            return False
        max_dict_word_length = max([len(x) for x in dict])
        f = [False] * (len(s) + 1)
        f[0] = True
        for i in range(1, len(s) + 1):
            for length_of_word in range(1, min(i, max_dict_word_length) + 1):
                if f[i - length_of_word] and s[i - length_of_word:i] in dict:
                    f[i] = True
        return f[len(s)]