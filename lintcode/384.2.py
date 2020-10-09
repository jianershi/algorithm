"""
384. Longest Substring Without Repeating Characters
https://www.lintcode.com/problem/longest-substring-without-repeating-characters/description

3. Longest Substring Without Repeating Characters
https://leetcode.com/problems/longest-substring-without-repeating-characters/
"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        n = len(s)
        seen = set()
        r = 0
        for l in range(n):
            while r < n and s[r] not in seen:
                res = max(res, r - l + 1)
                seen.add(s[r])
                r += 1
            seen.remove(s[l])
        return res