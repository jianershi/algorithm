"""
greedy solution won't work.

 [6, 4, 4, 6]
"""
import sys
class Solution:
    """
    @param A: An integer array
    @return: An integer
    """
    def stoneGame(self, A):
        # write your code here
        if not A:
            return 0
        sum_list = []
        self.sub_stone_game(A, sum_list)
        return sum(sum_list)


    def sub_stone_game(self, nums, sum_list):
        if len(nums) == 1:
            return
        two_sum_min_start_index, two_sum_min = None, sys.maxsize
        for i in range(len(nums) - 1):
            two_sum = nums[i] + nums[i + 1]
            if two_sum < two_sum_min:
                two_sum_min_start_index = i
                two_sum_min = two_sum
        sum_list.append(two_sum_min)
        # print(nums[0:two_sum_min_start_index] + [two_sum_min] + nums[two_sum_min_start_index + 2:])
        self.sub_stone_game(nums[0:two_sum_min_start_index] + [two_sum_min] + nums[two_sum_min_start_index + 2:], sum_list)

A= [6, 4, 4, 6] 

s = Solution()
print(s.stoneGame(A))
