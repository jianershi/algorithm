"""
1249. Minimum Remove to Make Valid Parentheses
https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/
"""
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        l, r = 0, 0
        op = 0
        stack = []
        for c in s:
            if c == '(':
                l += 1
                stack.append(c)
            elif c == ')':
                r += 1
                if r <= l:
                    stack.append(c)
                else:
                    op += 1
                    r -= 1
            else: #other char
                stack.append(c)
        
        l, r = 0, 0
        stack = stack[::-1]
        res = []
        for c in stack:
            if c == ')':
                r += 1
                res.append(c)
            elif c == '(':
                l += 1
                if l <= r:
                    res.append(c)
                else:
                    op += 1
                    l -= 1
            else: #other char
                res.append(c)
        
        res = "".join(res[::-1])
        print(op, res)
        return res        