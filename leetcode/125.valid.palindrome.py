"""
125. Valid Palindrome
remove all space and comma
"""
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # ''.join(str.filter
        newStr = ''.join(filter(str.isalnum, s)).lower()
        for i in range(len(newStr) // 2):
            if newStr[i] != newStr[len(newStr) - i -1]:
                return False
        return True