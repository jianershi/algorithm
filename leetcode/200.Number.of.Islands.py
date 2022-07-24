"""
200. Number of Islands
https://leetcode.com/problems/number-of-islands/

union?  <-probably but forgot how to implment
bfs
o(n)
"""
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        island_count = 0        
        visited = set()
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1" and ((i,j)) not in visited:
                    self.bfs(i, j, grid, visited)
                    island_count += 1
        return island_count
                    
    def bfs(self, i, j, grid, visited):
        queue = collections.deque([(i, j)])
        visited.add((i,j))
        
        while (queue):
            cur_x, cur_y = queue.popleft()
            for delta_x, delta_y in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
                new_x, new_y = cur_x + delta_x, cur_y + delta_y
                if self.isValid(new_x, new_y, grid, visited) and grid[new_x][new_y] == "1":
                    queue.append((new_x, new_y))
                    visited.add((new_x, new_y))
    
    def isValid(self, i, j, grid, visited):
        n = len(grid)
        m = len(grid[0])
        
        if i < 0 or i >= n:
            return False
        
        if j < 0 or j >= m:
            return False
        
        if (i, j) in visited:
            return False
        
        return True
        
        
                