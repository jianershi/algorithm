"""
1824. Most Frequent Substring
https://www.lintcode.com/problem/most-frequent-substring/description?_from=contest&&fromId=92
TLE
"""
class Solution:
    """
    @param s: string s
    @param minLength: min length for the substring
    @param maxLength: max length for the substring
    @param maxUnique: max unique letter allowed in the substring
    @return: the max occurrences of substring
    """
    def getMaxOccurrences(self, s, minLength, maxLength, maxUnique):
        # write your code here
        if not s or maxLength < 0 or maxUnique < 0 or len(s) < minLength:
            return 0

        minLength = max(1, minLength)

        max_occurance = {}
        unique_char = {}

        right = 0
        n = len(s)
        for left in range(n):
            while right < n and right - left < minLength:
                unique_char[s[right]] = unique_char.get(s[right], 0) + 1
                right += 1
            if right - left == minLength:
                if len(unique_char) <= maxUnique:
                    substring = s[left: right]
                    max_occurance[substring] = max_occurance.get(substring, 0) + 1
            unique_char[s[left]] -= 1
            if unique_char[s[left]] == 0:
                del unique_char[s[left]]
        return max(max_occurance.values()) if max_occurance else 0
