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
        hash = set()
        last_pair = (None, None)
        count = 0

        for num in nums:
            if target - num in hash and (target - num, num) != last_pair:
                count += 1
                last_pair = (target - num, num)
            hash.add(num)

        return count

# s = Solution()
# nums =  [1,1,2,45,46,46]
# target = 47
# answer = s.twoSum6(nums, target)
# print(s.twoSum6(nums, target))

import unittest
class Test(unittest.TestCase):
    s = Solution()

    def test1(self):
        nums =  [1,1,2,45,46,46]
        target = 47
        self.assertEqual(self.s.twoSum6(nums, target), 2)

    def test2(self):
        nums =  [1,1]
        target = 2
        self.assertEqual(self.s.twoSum6(nums, target), 1)

if __name__ == '__main__':
    unittest.main()
