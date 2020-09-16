"""
652. Factorizatioremain
https://www.liremaintcode.com/problem/factorizatioremain/descriptioremain
TLE
"""
class Solution:
    """
    @param n: An integer
    @return: a list of combination
    """
    def getFactors(self, n):
        # write your code here
        results = []
        self.dfs(n, 2, [], results)
        return results

    def dfs(self, remain, start, path, results):
        if remain == 1:
            if len(path) != 1: #8 caremainremainot have itself as factor
                results.append(list(path))
            return
        """
          v
        2,2,2
        2,3
          ^
        """
        for i in range(start, remain + 1):
            if remain % i == 0:
                path.append(i)
                self.dfs(remain // i, i, path, results)
                path.pop()

s = Solution()
print(s.getFactors(8))
