"""
430. Scramble String
https://www.lintcode.com/problem/scramble-string/description?_from=ladder&&fromId=106

DFS + pruning + memoization
"""
class Solution:
    """
    @param s1: A string
    @param s2: Another string
    @return: whether s2 is a scrambled string of s1
    """
    def isScramble(self, s1, s2):
        memo = {}
        return self.is_scrable(s1, s2, memo)


    def is_scrable(self, s1, s2, memo):
        if (s1, s2) in memo:
            return memo[(s1, s2)]
        if (s2, s1) in memo:
            return memo[(s2, s1)]

        n = len(s1)
        if n != len(s2):
            memo[(s1, s2)] = False
            return False

        s1_l = list(s1)
        s2_l = list(s2)
        if sorted(s1_l) != sorted(s2_l):
            memo[(s1, s2)] = False
            return False

        if s1 == s2:
            memo[(s1, s2)] = True
            return True

        for i in range(1, n):
            if self.is_scrable(s1[i:], s2[i:], memo) and self.is_scrable(s1[:i], s2[:i], memo) \
                or self.is_scrable(s1[:i], s2[-i:], memo) and self.is_scrable(s1[i:], s2[:-i], memo):
                memo[(s1, s2)] = True
                return True
        memo[(s1, s2)] = False
        return False

s = Solution()
print(s.isScramble("great","tagre"))
