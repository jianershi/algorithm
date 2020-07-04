"""
281. Paint the Ceiling
https://www.lintcode.com/problem/paint-the-ceiling/description?_from=contest&&fromId=94
周赛题
"""
class Solution:
    """
    @param s0: the number s[0]
    @param n: the number n
    @param k: the number k
    @param b: the number b
    @param m: the number m
    @param a: area
    @return: the way can paint the ceiling
    """
    def painttheCeiling(self, s0, n, k, b, m, a):
        # write your code here
        s = [s0]
        for i in range(1, n):
            s.append((k * s[i - 1] + b) % m + 1 + s[i - 1])
     
        n = len(s)
        j = n - 1
        count = 0
        for i in range(n):
            while j >= 0 and s[i] * s[j] > a:
                j -= 1 #j双指针可以倒过去走到0。反正比j小的*s[i]一定可以
                
            count += j + 1
      
        return count






s = Solution()
s0 = 2
n = 3
k = 3
b = 3
m = 2
a = 15
s.painttheCeiling(s0, n, k, b, m, a)
