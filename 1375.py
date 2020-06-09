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
        count = [0] * 256
        distinct_count = 0
        substring_count = 0
        for left in range(n):
            while right < n and distinct_count < k:
                count[ord(s[right])] += 1
                if count[ord(s[right])] == 1:
                    distinct_count += 1
                right += 1
            if distinct_count >= k:
                substring_count += n - right + 1
            count[ord(s[left])] -= 1
            if count[ord(s[left])] == 0:
                distinct_count -= 1
        return substring_count
