"""
415. Valid Palindrome
https://www.lintcode.com/problem/valid-palindrome/description
"""
class Solution:
    """
    @param s: A string
    @return: Whether the string is a valid palindrome
    """
    def isPalindrome(self, s):
        # write your code here
        # 先processs string to minimal format O(n)
        # 2跟指针，1跟从前往后，1跟从后往前。重合的时候就结束。
        # 总体时间法度 O(n)
        
        start, end = 0, len(s) - 1
        while start < end:
            #跳过无用字符
            while start < end and not s[start].isalpha() and not s[start].isnumeric(): start += 1
            while start < end and not s[end].isalpha() and not s[end].isnumeric(): end -= 1
            if s[start].lower() != s[end].lower():
                return False
            start += 1
            end -= 1
        return True
                