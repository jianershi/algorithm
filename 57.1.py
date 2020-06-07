"""
57. 3Sum
"""
class Solution:
    """
    @param numbers: Give an array numbers of n integer
    @return: Find all unique triplets in the array which gives the sum of zero.
    """
    def threeSum(self, numbers):
        # write your code here
        "暴力解 O(N^3), 如果只iterate 第一个数O(n)，那剩下的可以用two sum的解法，O(nlogn)"
        """
        a <= b <= c
        -a = b + c
        """
        numbers.sort() #O(n)
        result = []
        if len(numbers) <= 1:
            return result

        for i in range(len(numbers) - 2):
            if i > 0 and numbers[i] == numbers[i - 1]:
                continue
            self.two_sum(numbers, i + 1, len(numbers) - 1, -numbers[i], result)
        return result

    def two_sum(self, numbers, start, end, target, result):
        left, right = start, end
        while left < right:
            while left < right and numbers[left] + numbers[right] < target:
                left += 1
            while left < right and numbers[left] + numbers[right] > target:
                right -= 1
            if left < right and numbers[left] + numbers[right] == target:
                result.append([-target, numbers[left], numbers[right]])
                left += 1
                right -= 1
                while left < right and numbers[left] == numbers[left - 1]:
                    left += 1
                while left < right and numbers[right] == numbers[right + 1]:
                    right -= 1
