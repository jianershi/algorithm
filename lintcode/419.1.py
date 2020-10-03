"""
419. Roman to Integer
https://www.lintcode.com/problem/roman-to-integer/description
"""
class Solution:
    """
    @param s: Roman representation
    @return: an integer
    """
    def romanToInt(self, s):
        # write your code here
        CHAR_TO_DIGIT = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        
        prev = None
        ans = 0
        for c in s:
            if not prev or CHAR_TO_DIGIT[c] <= prev:
                ans = ans + CHAR_TO_DIGIT[c]
            else:
                ans = ans - 2 * prev + CHAR_TO_DIGIT[c]
            prev = CHAR_TO_DIGIT[c]
        return ans