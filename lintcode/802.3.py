"""
802. Sudoku Solver
https://www.lintcode.com/problem/sudoku-solver/description
DFS搜索顺序优化
"""
class Solution:
    """
    @param board: the sudoku puzzle
    @return: nothing
    """
    def solveSudoku(self, board):
        # write your code here
        
        self.dfs(board)

    """
    def searching start at the least choice position
    """
    def dfs(self, board):
        x, y, choices = self.get_least_choice_position(board)

        if x == None: #end, same as if index == 81:
            return True

        for num in choices:
            board[x][y] = num
            if self.dfs(board):
                return True
            board[x][y] = 0
        
        return False #if there is no choices, that means cannot reach end

    def get_least_choice_position(self, board):
        x, y, choices = None, None, [None] * 10

        for i in range(9):
            for j in range(9):
                if board[i][j] != 0:
                    continue
                choices_at_pos = []
                for num in range(1, 10):
                    if self.is_valid(num, i, j, board):
                        choices_at_pos.append(num)
                if len(choices_at_pos) < len(choices):
                    x, y, choices = i, j, choices_at_pos

        return x, y, choices

    def is_valid(self, num, x, y, board):
        for i in range(9):
            if board[i][y] == num:
                return False
            if board[x][i] == num:
                return False
            if board[x // 3 * 3 + i // 3][y // 3 * 3 + i % 3] == num:
                return False

        return True