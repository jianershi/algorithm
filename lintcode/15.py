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
        result = []
        if nums is None:
            return result
        visited = [False] * len(nums)
        self.dfs(nums, visited, [], result)
        return result
        
    """
    递归的定义:当前permutation开头的所有的排列
    """
    def dfs(self, nums, visited, permutation, result):
        #递归的出口。当前permutation的长度等于所有数组的长度。就是一个排列
        if len(permutation) == len(nums):
            result.append(list(permutation))
            return
        
        #递归的拆解。看其他的数有没有放到permutation里面去过，没放过就放进去。找下一层。
        for index in range(len(nums)):
            if visited[index]:
                continue
            permutation.append(nums[index])
            visited[index] = True
            self.dfs(nums, visited, permutation, result)
            visited[index] = False
            permutation.pop()