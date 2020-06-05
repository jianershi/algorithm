"""
419. Roman to Integer
method 1... save every combination...

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

        result = []
        for i in range(len(s)):
            if result and result[-1] < CHAR_TO_DIGIT[s[i]]:
                result[-1] = -result[-1]
            result.append(CHAR_TO_DIGIT[s[i]])

        return sum(result)

s = Solution()
print(s.romanToInt("IV"))
