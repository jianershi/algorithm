"""
301. Remove Invalid Parentheses
https://leetcode.com/problems/remove-invalid-parentheses/
@pololee detailed explanation:
https://leetcode.com/problems/remove-invalid-parentheses/discuss/75027/Easy-Short-Concise-and-Fast-Java-DFS-3-ms-solution

780. Remove Invalid Parentheses
https://www.lintcode.com/problem/remove-invalid-parentheses/description?_from=ladder&&fromId=160
九章强化班

"""
class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        res = []
        self.dfs(s, 0, 0, res, ['(', ')'])
        return res
    
    def dfs(self, s, scan_i, remove_j, res, pattern):
        n = len(s)
        count = 0
        for i in range(scan_i, n):
            if s[i] == pattern[0]:
                count += 1
            elif s[i] == pattern[1]:
                count -= 1
            if count >= 0:
                continue
            #removal needed
            for j in range(remove_j, i + 1):
                if s[j] == pattern[1] and (j == remove_j or s[j] != s[j - 1]):
                    self.dfs(s[:j] + s[j + 1:], i + 1 - 1, j + 1 - 1, res, pattern)
            return
        
        s = s[::-1]
        if pattern[0] == '(':
            self.dfs(s, 0, 0, res, pattern[::-1])
        else:
            res.append(s)
