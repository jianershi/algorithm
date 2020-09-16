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
        j = 0
        for i in range(n):
            while j < n and len(window_count) <= k:
                if s[j] not in window_count and len(window_count) == k:
                    break
                window_count[s[j]] = window_count.get(s[j], 0)
                window_count[s[j]] += 1
                j += 1
            max_length = max(max_length, j - i)
            window_count[s[i]] = window_count.get(s[i],0)
            window_count[s[i]] -= 1
            if window_count[s[i]] <= 0:
                del window_count[s[i]]
        return max_length
