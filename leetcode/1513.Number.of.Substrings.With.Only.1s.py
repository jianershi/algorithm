"""
1513. Number of Substrings With Only 1s
https://leetcode.com/problems/number-of-substrings-with-only-1s/description/
"""
class Solution:
    def numSub(self, s: str) -> int:
        if not s:
            return 0
        n = len(s)
        answer = 0
        j = 0
        M = int(1e9 + 7)
        for i in range(n):
            if s[i] != "1":
                continue
            j = max(j, i + 1)
            """
            optimization, instead of j = i + 1, i don't have to count from i + 1 to j again
               j
               v
            1110111
            ^
            i
             ^ <- anything between i and j is always 1, so it's just j - i
               j
            1110111
              ^i(last i before 0)
                 j <- move both i and j
            1110111
                i
            """
            while j < n and s[j] == "1":
                j += 1
            answer = (answer + j - i) % M

        return answer