"""
5. Longest Palindromic Substring
https://leetcode.com/problems/longest-palindromic-substring/
"""
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 0:
            return ""
        ret = ""
        for centerIndex in range(len(s)):
            even = self.getPalindromicString(centerIndex, centerIndex, s)
            if len(even) >= len(ret):
                ret = even
            odd = self.getPalindromicString(centerIndex, centerIndex + 1, s)
            if len(odd) >= len(ret):
                ret = odd
        return ret
                
    def getPalindromicString(self, left_center, right_center, s):
        l, r = left_center, right_center
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l + 1:r]
