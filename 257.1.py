"""
257. Longest String Chain
https://www.lintcode.com/problem/longest-string-chain/description?_from=contest&&fromId=93

dp[i] longest string chian ending in i
dp[i] = max(dp[i], dp[j] + 1) if distance between words[j] and word[i] is 1 for j in range [0, i)

max(dp[i])

dp[i] = 1

"""
class Solution:
    """
    @param words: the list of word.
    @return: the length of the longest string chain.
    """
    def longestStrChain(self, words):
        if not words:
            return 0

        words = sorted(words, key=lambda x: len(x))
        n = len(words)
        dp = [1] * n

        for i in range(n):
            for j in range(i - 1, -1 ,-1):
                # print (words[j], words[i], self.is_valid(words[j], words[i]))
                if len(words[j]) == len(words[i]):
                    continue
                if len(words[i]) - len(words[j]) > 1:
                    break
                if self.is_valid(words[j], words[i]):
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)

    def is_valid(self, word1, word2):
        if len(word2) - len(word1) > 1:
            return False
        i = 0
        j = 0
        while i < len(word1) and j < len(word2):
            if word1[i] == word2[j]:
                i += 1
                j += 1
            else:
                j += 1

        return i == len(word1) and j == len(word2) or i == len(word1) and j == len(word2) - 1