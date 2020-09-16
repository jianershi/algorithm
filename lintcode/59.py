"""
59. 3Sum Closest
https://www.lintcode.com/problem/3sum-closest/description

a + b + c closest to target
a + b cloeset to target - c
0 1  2 3 4 5
^   ^
"""
import sys
class Solution:
    """
    @param numbers: Give an array numbers of n integer
    @param target: An integer
    @return: return the sum of the three integers, the sum closest target.
    """
    def threeSumClosest(self, numbers, target):
        # write your code here
        numbers = sorted(numbers)
        n = len(numbers)
        min_diff = sys.maxsize
        min_diff_sum = sys.maxsize
        for i in range(n):
            left, right = 0, i - 1
            while left < right:
                diff = abs(numbers[left] + numbers[right] + numbers[i] - target)
                if diff < min_diff:
                    min_diff = diff
                    min_diff_sum = numbers[left] + numbers[right] + numbers[i]

                if left < right and numbers[left] + numbers[right] < target - numbers[i]:
                    left += 1
                elif left < right and numbers[left] + numbers[right] > target - numbers[i]:
                    right -= 1
                else:
                    break
        return min_diff_sum


s = Solution()
numbers = [-1,2,1,-4]
target = 1
print(s.threeSumClosest(numbers, target))
