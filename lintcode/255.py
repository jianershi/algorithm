"""
255. Multi-string search
https://www.lintcode.com/problem/multi-string-search/description
"""
class Solution:
    """
    @param sourceString: a string
    @param targetStrings: a string array
    @return: Returns a bool array indicating whether each string in targetStrings is a substring of the sourceString
    """
    def whetherStringsAreSubstrings(self, sourceString, targetStrings):
        # write your code here
        result = []
        for word in targetStrings:
            if word == "":
                result.append(True)
                continue
            if self.check_substring(sourceString, word):
                result.append(True)
            else:
                result.append(False)
        return result

    # def check_substring(self, source, target):
    #     m = len(source)
    #     n = len(target)
    #     for i in range(m - n + 1):    
    #         for j in range(n):
    #             if source[i + j] != target[j]:
    #                 break
    #         if j == n - 1 and source[i + j] == target[j]:
    #             return True
    #     return False
    def check_substring(self, source, target):
        m = len(source)
        n = len(target)
        i = j = 0
        while i < m and j < n:
            if source[i]!= target[j]:
                j = 0
            if source[i] == target[j]:
                i += 1
                j += 1
                continue
            i += 1
        if j == n:
            return True
        return False