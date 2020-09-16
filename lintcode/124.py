"""
124. Longest Consecutive Sequence
"""

class Solution:
    """
    @param num: A list of integers
    @return: An integer
    """
    def longestConsecutive(self, num):
        # write your code here
        if not num:
            return 0

        hash = set(num)

        max_count = 1

        for i_n in num:
            if i_n - 1 not in hash:
                count = 1
                while i_n + 1 in hash:
                    count += 1
                    i_n += 1
                max_count = max(count, max_count)

        return max_count
