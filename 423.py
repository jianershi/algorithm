"""
423. Valid Parentheses
https://www.lintcode.com/problem/valid-parentheses/description?_from=ladder&&fromId=37
"""
class Solution:
    """
    @param s: A string
    @return: whether the string is a valid parentheses
    """
    def isValidParentheses(self, s):
        # write your code here
        stack  = []
        for c in s:
            if c == '(' or c == '[' or c == '{':
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                top = stack.pop()
                if top == '(' and c != ')':
                    return False
                if top == '[' and c != ']':
                    return False
                if top == '{' and c != '}':
                    return False
        return not stack