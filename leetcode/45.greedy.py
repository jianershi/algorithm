"""
45. Jump Game II
https://leetcode.com/problems/jump-game-ii/
greedy, bfs
problem always assumes i can reach the end
"""
class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        steps = 0
        current_reach = 0
        next_reach = 0
        for i in range(n):
            if i > current_reach:
                steps += 1
                current_reach = next_reach
            next_reach = max(next_reach, nums[i] + i)
                
        return steps