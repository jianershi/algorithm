"""
384. Longest Substring Without Repeating Characters
https://www.lintcode.com/problem/longest-substring-without-repeating-characters/description

3. Longest Substring Without Repeating Characters
https://leetcode.com/problems/longest-substring-without-repeating-characters/
"""
"""
0123
abcb
^  ^ 
"""
class Solution:
    """
    @param s: a string
    @return: an integer
    """
    def lengthOfLongestSubstring(self, s):
        # write your code here
        count = {}
        
        max_len = 0
        l = 0
        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1
            while l < r and count[s[r]] > 1:
                count[s[l]] -= 1
                l += 1
            if count[s[r]] == 0:
                del count[s[r]]
            max_len = max(max_len, r - l + 1)
        return max_len