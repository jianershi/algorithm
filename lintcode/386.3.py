"""
386. Longest Substring with At Most K Distinct Characters
2nd try
"""
class Solution:
    """
    @param s: A string
    @param k: An integer
    @return: An integer
    """
    def lengthOfLongestSubstringKDistinct(self, s, k):
        window_count = {}
        max_length = 0
        n = len(s)
        left = 0
        for right in range(n):
            window_count[s[right]] = window_count.get(s[right], 0)
            window_count[s[right]] += 1
            while left < right and len(window_count) > k:
                window_count[s[left]] -= 1
                if window_count[s[left]] == 0:
                    del window_count[s[left]]
                left += 1
            if len(window_count) <= k:
                max_length = max(max_length, right - left + 1)

        return max_length
