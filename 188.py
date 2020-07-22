"""
188. Insert five
https://www.lintcode.com/problem/insert-five/description?_from=ladder&&fromId=37
"""
class Solution:
    """
    @param a: A number
    @return: Returns the maximum number after insertion
    """
    def InsertFive(self, a):
        # write your code here

        if a >= 0:
            s_a = str(a)
            n = len(s_a)
            for i in range(n):
                if s_a[i] <= '5':
                    break
            ans = s_a[:i] + '5' + s_a[i:]
            return (int(ans))

        if a < 0:
            s_a = str(-a)
            n = len(s_a)
            for i in range(n):
                if s_a[i] >= '5':
                    break
            ans = s_a[:i] + '5' + s_a[i:]
            return (-int(ans))