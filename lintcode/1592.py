"""
1592. Rearrange Spaces Between Words
https://leetcode.com/contest/weekly-contest-207/problems/rearrange-spaces-between-words/
"""
class Solution:
    def reorderSpaces(self, text: str) -> str:
        s = text.split()
        charL = len("".join(s))
        lenS = len(text) - charL
        if len(s) > 1:
            betweenWord = lenS // (len(s) - 1)
            res = (" " * betweenWord).join(s)
        else:
            res = "".join(s)

        while len(res) < len(text):
            res += " "

        return res

