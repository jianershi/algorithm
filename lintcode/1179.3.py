"""
1179. Friend Circles
2nd round
https://www.lintcode.com/problem/friend-circles/description?_from=ladder&&fromId=152

thought:
connected components - bfs
union find
strongly connected components? first compress the graph n^3, then searching through graph n^2....hmm.. maybe not

"""
from collections import deque
class Solution:
    """
    @param M: a matrix
    @return: the total number of friend circles among all the students
    """
    def findCircleNum(self, M):
        # Write your code here
        """
        m is just adj matrix
        """
        if not M:
            return 0
        count = 0
        
        n = len(M)

        v = set()

        for i in range(n):
            if i in v:
                continue
            count += 1
            self.bfs(i, v, M)
        
        return count

    def bfs(self, i, v, M):
        q = deque([i])
        v.add(i)
        while q:
            f = q.popleft()
            for i, n in enumerate(M[f]):
                if n == 0:
                    continue
                if i in v:
                    continue
                
                q.append(i)
                v.add(i)
