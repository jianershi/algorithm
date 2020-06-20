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

        n = len(s)

        for i in range(minLength - 1):
            unique_char[s[i]] = unique_char.get(s[i], 0) + 1

        for left in range(n - minLength + 1):
            right = left + minLength - 1
            unique_char[s[right]] = unique_char.get(s[right], 0) + 1
            if len(unique_char) <= maxUnique:
                substring = s[left: right + 1]
                max_occurance[substring] = max_occurance.get(substring, 0) + 1
            unique_char[s[left]] -= 1
            if unique_char[s[left]] == 0:
                del unique_char[s[left]]
        return max(max_occurance.values()) if max_occurance else 0
