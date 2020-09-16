from collections import deque

class Solution:
    """
    @param grid: a boolean 2D matrix
    @return: an integer
    """
    def numIslands(self, grid):
        # write your code here
        """
        由点及面问题
        traverse entire 2D Matrix.
        for each point, put in BFS(with visited)
        """
        island = 0
        visited = set()

        for row_i in range(len(grid)):
            for column_i in range(len(grid[0])):
                if grid[row_i][column_i] and (row_i, column_i) not in visited: #遇到是1的点，从那个点开始做bfs. 但是保持一个全局的visited 防止重复岛屿
                    self.bfs(grid, visited, row_i, column_i)
                    island += 1

        return island

    """
    围绕一个点（root)进行BFS搜索
    如果隔壁的点访问过则跳过，没访问过驾到队列里展开。
    只对是1的点进行操作，0的点默认掠过
    """
    def bfs(self, grid, visited, row_i, column_i):
        queue = deque([(row_i, column_i)])
        visited.add((row_i, column_i))

        while (queue):
            (head_x, head_y) = queue.popleft()
            for delta_vect_x, delta_vect_y in [(1, 0), (0, -1), (-1, 0), (0, 1)]: #上下左右
                new_location_index = (head_x + delta_vect_x, head_y + delta_vect_y)
                if not (self.check_valid(new_location_index, grid, visited)):
                    continue
                visited.add(new_location_index)
                queue.append(new_location_index)


    def check_valid(self, location, grid, visited):
        if location[0] < 0 or location[0] >= len(grid):
            return False
        if location[1] < 0 or location[1] >= len(grid[0]):
            return False
        if location in visited:
            return False
        # print (location)
        return grid[location[0]][location[1]]
