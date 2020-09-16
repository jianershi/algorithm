"""
1375. Substring With At Least K Distinct Characters
"""

class Solution:
    """
    @param s: a string
    @param k: an integer
    @return: the number of substrings there are that contain at least k distinct characters
    """
    def kDistinctCharacters(self, s, k):
        # Write your code here
        n = len(s)
        right = 0
        count = {}
        substring_count = 0
        for left in range(n):
            while right < n and len(count) < k:
                count[ord(s[right])] = count.get(ord(s[right]), 0) + 1
                right += 1
            if len(count) >= k:
                substring_count += n - right + 1
            count[ord(s[left])] -= 1
            if count[ord(s[left])] == 0:
                del count[ord(s[left])]
        return substring_count
