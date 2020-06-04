"""
194. Find Words
see note
"""
class Solution:
    """
    @param str: the string
    @param dict: the dictionary
    @return: return words which  are subsequences of the string
    """
    def findWords(self, str, dict):
        # Write your code here.
        if not str or not dict:
            return []

        n = len(str)
        results = []

        next_char = self.build_next_char(str)

        for word in dict:
            i = 0
            j = 0
            m = len(word)
            while i < n and j < m:
                i = next_char[i][ord(word[j]) - ord('a')]
                if i == n:
                    break
                j += 1
            if j == m:
                results.append(word)

        return results

    """
    if not found, default to len(str)
    """
    def build_next_char(self, str):
        n = len(str)
        next_char = [[n] * 26 for _ in range(n + 1)]
        for i in range(n - 1, -1, -1):
            for j in range(26):
                next_char[i][j] = next_char[i + 1][j]
                if ord(str[i]) - ord('a') == j:
                    next_char[i][j] = i
        return next_char

s = Solution()
       # 0123456789012345678920
str = "bcogtadsjofisdhklasdj"
dict=["book","code","tag"]
print (s.findWords(str, dict))
