"""
123. Word Search
https://www.lintcode.com/problem/word-search/description?_from=ladder&&fromId=37

"""
DIRECTIONS = [
    (0, 1),
    (0, -1),
    (-1, 0),
    (1, 0)
]

from collections import deque
class Solution:
    """
    @param board: A list of lists of character
    @param word: A string
    @return: A boolean
    """
    def exist(self, board, word):
        # write your code here
        if not board or not board[0]:
            return False
            
        n = len(board)
        m = len(board[0])
        
        for i in range(n):
            for j in range(m):
                if board[i][j] == word[0]:
                    if self.dfs(board, i, j, set([(i,j)]), word, 0):
                        return True
        return False
    
    def dfs(self, board, i, j, path, word, index):
        if index == len(word) - 1:
            return True
        
        n = len(board)
        m = len(board[0])
        
        for delta_x, delta_y in DIRECTIONS:
            nx, ny = i + delta_x, j + delta_y
            if not self.is_valid(nx, ny, n, m, path):
                continue
            if board[nx][ny] == word[index + 1]:
                path.add((nx, ny))
                if self.dfs(board, nx, ny, path, word, index + 1):
                    return True
                path.remove((nx,ny))
        
        return False
        
    def is_valid(self, x, y, n, m, path):
        if (x, y) in path:
            return False
        if not (0 <= x < n and 0 <= y < m):
            return False
        return True