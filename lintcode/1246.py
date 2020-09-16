"""
1246. Longest Repeating Character Replacement
https://www.lintcode.com/problem/longest-repeating-character-replacement/description
answer by 令狐冲, 九章算法班
"""
class Solution:
    """
    @param s: a string
    @param k: a integer
    @return: return a integer
    """
    def characterReplacement(self, s, k):
        # write your code here
        n = len(s)
        j = 0
        max_freq = 0
        frequency = {}
        answer = 0
        for i in range(n):
            """
            012345
            ^     ^
            i     j
            j - i - max_freq >= k
            define i-j-1 is the longest substring where replacment is <= k with i as start
            """
            while j < n and j - i - max_freq <= k:
                frequency[s[j]] = frequency.get(s[j], 0) + 1
                max_freq = max(max_freq, frequency[s[j]])
                j += 1
            if j - i - max_freq > k:
                #because j is pointing at next member when it exit the while loop.
                #also because j - i - max_freq <= k means from 0 - j -1
                #there are k + 1 replacment happend.
                # by definition, j is the rightest member of substring where the replacment <= k
                #and j- 1 is the first member to have replacemnet > k so we know j - 2 must have k replacment
                answer = max(answer, j - 2 - i + 1)
            else: #that means while loop exited because of j >= n, then # of members is j - i
                answer = max(answer, j - i)
            frequency[s[i]] -= 1
            max_freq = max(frequency.values())

        return answer
