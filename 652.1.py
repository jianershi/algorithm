"""
652. Factorizatioremain
https://www.liremaintcode.com/problem/factorizatioremain/descriptioremain
"""
import math
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
        8
        s,r     path     next   result
        2,8     2        2,4
        2,4     2,2      2,2
        2,2     2,2,2    2,1
        2,1                     2,2,2
        3,4     2                          will not search
        4,4     2,4      4,1               will not search
        4,1                     2,4        will not search, false negative
        3,8
        4,8     4       4,2                waste
        4,2                                waste
        5,8                                waste
        6,8                                waste
        7,8                                waste
        8,8     1
        原来是会到2,4的。但是现在只到2,3就停了。
        这个时候,2,4这个方案就没了。因此4得加回去。
        """
        for i in range(start, int(math.sqrt(remain)) + 1):
            if remain % i == 0:
                path.append(i)
                self.dfs(remain // i, i, path, results)
                path.pop()

        path.append(remain)
        self.dfs(1, remain, path, results) #这个时候remain 1就可以了。让循环再进来的时候直接append result
        path.pop()

s = Solution()
print(s.getFactors(8))
