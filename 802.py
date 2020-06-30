"""
802. Sudoku Solver
https://www.lintcode.com/problem/sudoku-solver/description
"""
class Solution:
    """
    @param board: the sudoku puzzle
    @return: nothing
    """
    def solveSudoku(self, board):
        # write your code here
        self.dfs(0, board)

    def dfs(self, index, board):
        if index == 81:
            return True

        x = index // 9
        y = index % 9
        if board[x][y] != 0:
            return self.dfs(index + 1, board)

        for num in range(1, 10):
            if not self.is_valid(num, x, y, board):
                continue
            
            board[x][y] = num
            if self.dfs(index + 1, board):
                return True
            board[x][y] = 0
        
        return False
        
    def is_valid(self, num, x, y, board):
        for i in range(9):
            if board[x][i] == num: #check every row
                return False
            if board[i][y] == num: #chekc every col
                return False
            if board[x // 3 * 3 + i // 3][y // 3 * 3 + i % 3] == num:
                return False

        return True