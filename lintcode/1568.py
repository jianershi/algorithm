"""
1568. Minimum Number of Days to Disconnect Island
https://leetcode.com/problems/minimum-number-of-days-to-disconnect-island/
"""
class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        land = self.count_land(grid)
        if not self.isOneIsland(grid, land):
            return 0
        n, m = len(grid), len(grid[0])
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    grid[i][j] = 0
                    if not self.isOneIsland(grid, land - 1):
                        return 1
                    grid[i][j] = 1
        return 2
    
    def count_land(self, grid):
        n, m = len(grid), len(grid[0])
        count = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    count += 1
        return count
    
    def isOneIsland(self, grid, land):
        n, m = len(grid), len(grid[0])
        count = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    count = self.bfs(grid, i, j)
                    return count == land
        return False
    
    def bfs(self, grid, x, y):
        DIRECTIONS = [
            (0, 1),
            (0, -1),
            (-1, 0),
            (1, 0)
        ]
        n, m = len(grid), len(grid[0])
        q = deque([(x,y)])
        v = set([(x,y)])
        count = 0
        while q:
            x, y = q.popleft()
            count += 1
            for delta_x, delta_y in DIRECTIONS:
                nx, ny = x + delta_x, y + delta_y
                if not self.is_valid(nx, ny, grid, v):
                    continue
                q.append((nx,ny))
                v.add((nx,ny))
        return count
    
    def is_valid(self, x, y, grid, v):
        n, m = len(grid), len(grid[0])
        if (x < 0 or x >= n or y < 0 or y >= m):
            return False
        if (x, y) in v:
            return False
        if grid[x][y] == 0:
            return False
        return True