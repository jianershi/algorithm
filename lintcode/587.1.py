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
        last_pair = (None, None)
        for i in range(len(nums)):
            if target - nums[i] in hash and (target - nums[i], nums[i]) != last_pair:
                count += 1
                last_pair = (target - nums[i], nums[i])
            hash.add(nums[i])

        return count

s = Solution()
nums =  [1,1,2,45,46,46]
target = 47
print(s.twoSum6(nums, target))
