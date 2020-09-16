"""
271. prefix notation to postfix notation
https://www.lintcode.com/problem/prefix-notation-to-postfix-notation/description?_from=contest&&fromId=94
https://www.geeksforgeeks.org/prefix-postfix-conversion/
"""
from collections import deque
class Solution:
    """
    @param str: the prefix notation.
    @return: return the postfix notation.
    """
    def prefixNotationToPostfixNotation(self, str):
        # write your code here.
        if not str:
            return ""

        stack = []
        str = str.split(" ")[::-1]

        operator = set(["+","-","*","/"])

        for i in str:
            if i in operator:
                op1 = stack.pop()
                op2 = stack.pop()

                stack.append(op1 + " " + op2 + " " + i)
            else:
                stack.append(i)
        return stack[0]


s = Solution()
str = "+ * A B * C D"
print(s.prefixNotationToPostfixNotation(str))