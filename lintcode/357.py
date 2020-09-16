"""
357. Symmetrical Suffix
https://www.lintcode.com/problem/symmetrical-suffix/description?_from=contest&&fromId=103
tle
"""
class Solution:
    """
    @param s: a string.
    @return: return the values of all the intervals.
    """
    def suffixQuery(self, s):
        # write your code here
        n = len(s)
        counter = 0
        for i in range(n):   
            for r_start in range(n - 1, i - 1, -1):
                c = 0
                l, r = i, r_start
                while i <= l <= r_start and i <= r <= r_start:
                    if s[l] == s[r]:
                        l += 1
                        r -= 1
                        c += 1
                    else:
                        break
                counter += c
        return counter
