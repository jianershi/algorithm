"""
575. Decode String
https://www.lintcode.com/problem/decode-string/description
"""
class Solution:
    """
    @param s: an expression includes numbers, letters and brackets
    @return: a string
    """
    def expressionExpand(self, s):
        # write your code here
        stack = []
        number = 0
        for c in s:
            if c.isdigit():
                number = 10 * number + (ord(c) - ord('0'))
            elif c == '[':
                stack.append(number)
                number = 0
            elif c == ']':
                reversed_c = []
                while stack and not isinstance(stack[-1], int):
                    reversed_c.append(stack.pop())
                for _ in range(stack.pop()):
                    stack.extend(reversed_c[::-1])
            else:
                stack.append(c)
        return "".join(stack)
