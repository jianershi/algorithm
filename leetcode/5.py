"""
5. Longest Palindromic Substring
https://leetcode.com/problems/longest-palindromic-substring/

200. Longest Palindromic Substring
https://www.lintcode.com/problem/longest-palindromic-substring/my-submissions
"""
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        start = end = 0
        for c in range(n):
            l, r = self.search(c, c, s)
            if r - l > end - start:
                start, end = l, r
            l, r = self.search(c, c + 1, s)
            if r - l > end - start:
                start, end = l, r
            
        return s[start: end + 1]
    
    def search(self, l, r, s):
        n = len(s)
        while l >= 0 and r < n:
            if s[l] != s[r]:
                break
            l -= 1
            r += 1
        
        return l + 1, r - 1