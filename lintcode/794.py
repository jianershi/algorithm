"""
794. Sliding Puzzle II
https://www.lintcode.com/problem/sliding-puzzle-ii/description?_from=ladder&&fromId=160
"""
from collections import deque
DIRECTIONS = [
    (0, 1),
    (0, -1),
    (-1, 0),
    (1, 0)
]
class Solution:
    """
    @param init_state: the initial state of chessboard
    @param final_state: the final state of chessboard
    @return: return an integer, denote the number of minimum moving
    """
    def minMoveStep(self, init_state, final_state):
        # # write your code here
        if not init_state or not final_state:
            return -1
        if len(init_state) != 3 or len(init_state[0]) != 3:
            return -1
        if len(final_state) != 3 or len(final_state[0]) != 3:
            return -1

        init_state_string = self.state_to_string(init_state)
        final_state_string = self.state_to_string(final_state)

        queue = deque([(init_state_string, 0)])
        visited = set([init_state_string])

        while queue:
            curr_state_str, dist = queue.popleft()
            zero_x, zero_y = self.find_zero(curr_state_str)
            if (zero_x, zero_y) == (-1, -1):
                return -1
            for delta_x, delta_y in DIRECTIONS:
                next_x = zero_x + delta_x
                next_y = zero_y + delta_y
                if not self.is_valid(next_x, next_y):
                    continue
                next_state_string = self.go_next(zero_x, zero_y, next_x, next_y, curr_state_str)
                if next_state_string in visited:
                    continue
                if next_state_string == final_state_string:
                    return dist + 1
                queue.append((next_state_string, dist + 1))
                visited.add(next_state_string)
        return -1

    def state_to_string(self, state):
        state_string = ""
        for i in range(3):
            for j in range(3):
                state_string += str(state[i][j])
        return state_string

    def find_zero(self, state_string):
        index = state_string.find('0')
        if index == -1: #exception
            return (-1, -1)
        return index // 3, index % 3

    def is_valid(self, x, y):
        return (0 <= x < 3 and 0 <= y < 3)

    def go_next(self, zero_x, zero_y, next_x, next_y, curr_state_str):
        curr_state_list = list(curr_state_str)
        new_state_list = [x for x in curr_state_str]

        index_zero = zero_x * 3 + zero_y
        index_next = next_x * 3 + next_y
        new_state_list[index_zero], new_state_list[index_next] = new_state_list[index_next], new_state_list[index_zero]

        new_string = ""
        for i in new_state_list:
            new_string += i
        return new_string

s = Solution()
init_state = [
 [2,8,3],
 [1,0,4],
 [7,6,5]
]
final_state = [
 [1,2,3],
 [8,0,4],
 [7,6,5]
]
print(s.minMoveStep(init_state, final_state))
