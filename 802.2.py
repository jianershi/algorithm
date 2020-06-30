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
        
        self.dfs(board, self.build_used(board))

    def build_used(self, board):
        used = {
            "row": [set() for _ in range(9)],
            "col": [set() for _ in range(9)],
            "box": [set() for _ in range(9)]
        }

        for i in range(9):
            for j in range(9):
                if board[i][j] != 0:
                    self.mark_used(i, j, board, used, unmark=False)

        return used        

    def mark_used(self, i, j, board, used, unmark=False):
        if unmark == False:
            used["row"][i].add(board[i][j])
            used["col"][j].add(board[i][j])
            used["box"][i // 3 * 3 + j // 3].add(board[i][j])
        else:
            used["row"][i].remove(board[i][j])
            used["col"][j].remove(board[i][j])
            used["box"][i // 3 * 3 + j // 3].remove(board[i][j])

    """
    def searching start at the least choice position
    """
    def dfs(self, board, used):
        x, y, choices = self.get_least_choice_position(board, used)

        if x == None: #end, same as if index == 81:
            return True

        for num in choices:
            board[x][y] = num
            self.mark_used(x, y, board, used)
            if self.dfs(board, used):
                return True
            self.mark_used(x, y, board, used, unmark=True)
            board[x][y] = 0
        
        return False #if there is no choices, that means cannot reach end

    def get_least_choice_position(self, board, used):
        x, y, choices = None, None, [None] * 10

        for i in range(9):
            for j in range(9):
                if board[i][j] != 0:
                    continue
                choices_at_pos = []
                for num in range(1, 10):
                    if self.is_valid(num, i, j, board, used):
                        choices_at_pos.append(num)
                if len(choices_at_pos) < len(choices):
                    x, y, choices = i, j, choices_at_pos

        return x, y, choices

    def is_valid(self, num, x, y, board, used):
        if num in used["row"][x] or num in used["col"][y] or num in used["box"][x // 3 * 3 + y // 3]:
            return False

        return True