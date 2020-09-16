"""
587. Two Sum - Unique pairs
"""
class Solution:
    """
    @param nums: an array of integer
    @param target: An integer
    @return: An integer
    """
    def twoSum6(self, nums, target):
        # write your code here
        nums = sorted(nums)
        count = 0
        hash = set()
        visited = set()
        for i in range(len(nums)):
            if target - nums[i] in hash and nums[i] not in visited:
                count += 1
                visited.add(nums[i])
            hash.add(nums[i])

        return count

s = Solution()
nums =  [1,1]
target = 2
print(s.twoSum6(nums, target))
