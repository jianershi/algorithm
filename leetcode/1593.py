"""
1593. Split a String Into the Max Number of Unique Substrings
https://leetcode.com/contest/weekly-contest-207/problems/split-a-string-into-the-max-number-of-unique-substrings/
"""
class Solution:
    def __init__(self):
        self.max_len = 0

    def maxUniqueSplit(self, s: str) -> int:
        self.dfs(0, s, set(), 0, [])
        return self.max_len

    def dfs(self, index, s, used, lastcut, path):
        if len("".join(path)) == len(s):
            self.max_len = max(self.max_len, len(path))

        n = len(s)
        for i in range(index, n):
            if s[lastcut: i + 1] in used:
                continue
            chars = s[lastcut: i + 1]
            path.append(chars)
            used.add(chars)
            self.dfs(i + 1, s, used, i + 1, path)
            used.remove(chars)
            path.pop()
