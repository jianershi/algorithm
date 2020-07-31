"""
1221. Concatenated Words
https://www.lintcode.com/problem/concatenated-words/description?_from=ladder&&fromId=131

word break ii 变形题
"""

class Solution:
    """
    @param words: List[str]
    @return: return List[str]
    """
    def findAllConcatenatedWordsInADict(self, words):
        # write your code here
        word_set = set([w for w in words if len(w) > 0])
        result = []
        for word in words:
            if len(word) == 0:
                continue
            word_set.remove(word)
            if self.dfs(word, 0, words, word_set):
                result.append(word)
            word_set.add(word)
        return result
        
    def dfs(self, target, index, words, word_set):
        if index == len(target):
            return True
            
        for i in range(index + 1, len(target) + 1):
            prefix = target[index: i]
            if prefix not in word_set:
                continue
            if self.dfs(target, i, words, word_set):
                return True
        return False