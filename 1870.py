"""
1870. number of substrings with all zeroes
https://www.lintcode.com/problem/number-of-substrings-with-all-zeroes/description
"""
class Solution:
    """
    @param str: the string
    @return: the number of substrings
    """
    def stringCount(self, str):
        # Write your code here.
        n = len(str)
        j = 0
        count = 0
        for i in range(n):
            j = max(j, i + 1)
            if str[i] != '0':
                continue
            while j < n and str[j] == '0':
                j += 1
            count += j - i
        return count
