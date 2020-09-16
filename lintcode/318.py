"""
318. Character Grid
https://www.lintcode.com/problem/character-grid/description
"""
class Solution:
    """
    @param A: A string
    @param B: A string
    @return: A string array
    """
    def characterGrid(self, A, B):
        # write your code here.
        n = len(A)
        m = len(B)
        
        found_index = None, None
        for i, c in enumerate(A):
            found = False
            index = None
            for j in range(m):
                if B[j] == c:
                    found = True
                    index = j
                    break
            if found:
                found_index = i, index
                break
        res = [["."] * n for _ in range(m)]
        a, b = found_index
        for i in range(n):
            res[b][i] = A[i]
        for i in range(m):
            res[i][a] = B[i]
        
        res2 = []
        for line in res:
            res2.append("".join(line))
        return res2
                
                
s = Solution()
A = "BANANA"
B = "APPLE"
print(s.characterGrid(A, B))