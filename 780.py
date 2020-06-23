"""
780. Remove Invalid Parentheses
https://www.lintcode.com/problem/remove-invalid-parentheses/description?_from=ladder&&fromId=160
九章强化班
"""
PATTERN = [
    ['(',')'],
    [')','(']
]
class Solution:
    """
    @param s: The input string
    @return: Return all possible results
    """
    def removeInvalidParentheses(self, s):
        # Write your code here
        results = []
        self.dfs(s, 0, 0, PATTERN[0], results)
        return results

    def dfs(self, s, start, last_removal, pattern, results):
        n = len(s)
        count = 0

        for i in range(start, n):
            if s[i] == pattern[0]:
                count += 1
            elif s[i] == pattern[1]:
                count -= 1

            if count < 0:
                for j in range(last_removal, i + 1):
                    if s[j] == pattern[1] and (j == last_removal or s[j] != s[j - 1]):
                        self.dfs(s[:j] + s[j + 1:], i, j, pattern, results)
                return #因为此时，原来的字符串已经处理完了。无法再继续处理下去（字符串改变了）

        s = s[::-1]

        if pattern[0] == PATTERN[0][0]:
            self.dfs(s, 0, 0, PATTERN[1], results)
        else:
            results.append(s)