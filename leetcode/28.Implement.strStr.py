class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack)):
            for j in range(min(len(needle), len(haystack) - i)): # i + j < len(haystack)
                if haystack[i + j] != needle[j]:
                    break
                if j == len(needle) - 1: #reaches last character
                    return i
        return -1   