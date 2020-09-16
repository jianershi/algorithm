"""
386. Longest Substring with At Most K Distinct Characters
"""
class Solution:
    """
    @param s: A string
    @param k: An integer
    @return: An integer
    """
    def lengthOfLongestSubstringKDistinct(self, s, k):
        # write your code here
        count = [0] * 256
        distinct_count = 0

        n = len(s)
        left = 0
        max_length = 0
        for right in range(n):
            count[ord(s[right])] += 1
            if count[ord(s[right])] == 1:
                distinct_count += 1
            while left <= right and distinct_count > k:
                count[ord(s[left])] -= 1
                if count[ord(s[left])] == 0:
                    distinct_count -= 1
                left += 1
            if distinct_count <= k:
                max_length = max(max_length, right - left + 1)
        return max_length
