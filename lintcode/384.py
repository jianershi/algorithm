"""
384. Longest Substring Without Repeating Characters
https://www.lintcode.com/problem/longest-substring-without-repeating-characters/description

3. Longest Substring Without Repeating Characters
https://leetcode.com/problems/longest-substring-without-repeating-characters/
"""
class Solution:
    """
    @param s: a string
    @return: an integer
    """
    def lengthOfLongestSubstring(self, s):
        # write your code here
        appeared = [False] * 256
        n = len(s)
        right = 0
        max_length = 0
        for left in range(n):
            while right < n and not appeared[ord(s[right])]:
                appeared[ord(s[right])] = True
                max_length = max(max_length, right - left + 1)
                right += 1

            appeared[ord(s[left])] = False
        return max_length
