"""
1179. Friend Circles

https://www.lintcode.com/problem/friend-circles/description

BFS
"""
from collections import deque
class Solution:
    """
    @param M: a matrix
    @return: the total number of friend circles among all the students
    """
    def findCircleNum(self, M):
        # Write your code here

        visited = set()
        count = 0
        for person_id in range(len(M)):
            if person_id in visited:
                continue
            count += 1
            self.bfs(person_id, M, visited)
        return count

    def bfs(self, person_id, M, visited):
        queue = deque()
        queue.append(person_id)
        visited.add(person_id)
        while queue:
            now_id = queue.popleft()
            for friend_id, is_friend in enumerate(M[now_id]):
                if friend_id in visited:
                    continue
                if is_friend:
                    queue.append(friend_id)
                    visited.add(friend_id)
