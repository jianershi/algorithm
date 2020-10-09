"""
55. Jump Game
https://leetcode.com/problems/jump-game/
greedy
o(n)
"""
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        reach = 0
        for i in range(n):
            if i > reach:
                break
            reach = max(reach, nums[i] + i)
        return reach >= n - 1