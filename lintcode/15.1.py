"""
15. Permutations
https://www.lintcode.com/problem/permutations/my-submissions
"""
class Solution:
    """
    @param: nums: A list of integers.
    @return: A list of permutations.
    """
    def permute(self, nums):
        # write your code here
        res = []
        self.dfs(nums, [], res, set())
        return res
    
    def dfs(self, nums, path, res, visited):
        n = len(nums)
        if len(path) == n:
            res.append(list(path))
            return
        
        for i in range(n):
            if i in visited:
                continue
            path.append(nums[i])
            visited.add(i)
            self.dfs(nums, path, res, visited)
            visited.remove(i)
            path.pop()