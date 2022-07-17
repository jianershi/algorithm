"""
 dynamic programming
 time limit exceeded
 definition:
 d[i][j] = whether s[i][j] is palindrone
 d[i][j] = d[i + 1][j - 1] and s[i] == s[j]
 direction: len from small to large
 initialization:
 d[i][i] = true
 d[i][i + 1] = s[i] == s[i + 1]
 answer:
 s[max_i, max_j + 1]
"""
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return s
        
        n = len(s)
        d = [[False] * n for _ in range(n)]
        max_i, max_j = 0, 0
        for i in range(n):
            d[i][i] = True; #is true for a single character  
        for i in range(n - 1): #for lengh of 1
            d[i][i + 1] = s[i] == s[i + 1]
            if d[i][i + 1]:
                max_i, max_j = i, i + 1           
        
        for pal_len in range(3, n + 1): #iterate len from small to large
            for i in range(n - pal_len + 1): #define start
                j = i + pal_len - 1 #define end
                # if j - 1 < i + 1:
                #     break
                #d[0][1] = d[1][0]
                #d[0][1] = d[1][0] <<--- because the loop doesn't cover lengh of 1, thus initalization is needed for this case
                #aba
                #d[0][2] = d[1][1] and s[0] == s[2]
                #daab
                #d[0][3] = d[1][2] and s[0] == s[2]
                d[i][j] = d[i + 1][j - 1] and s[i] == s[j]
                if d[i][j] and j - i > max_j - max_i:
                    max_i, max_j= i, j
        
        return s[max_i: max_j + 1]