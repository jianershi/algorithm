"""
57. 3Sum
-a = b + c
"""
class Solution:
    """
    @param numbers: Give an array numbers of n integer
    @return: Find all unique triplets in the array which gives the sum of zero.
    """
    def threeSum(self, numbers):
        if not numbers:
            return []
        results = []

        numbers = sorted(numbers)

        for i in range(len(numbers)):
            if i > 0 and numbers[i] == numbers[i - 1]:
                continue
            self.two_sum(numbers, i + 1, -numbers[i], results)

        return results

    def two_sum(self, numbers, starting_index, target, results):
        left, right = starting_index, len(numbers) - 1

        while left < right: # < or < =
            while left < right and left - starting_index > 0 and numbers[left] == numbers[left - 1]:
                left += 1
            while left < right and right < len(numbers) - 1 and numbers[right] == numbers[right + 1]:
                right -= 1
            while left < right and numbers[left] + numbers[right] < target:
                left += 1
            while left < right and numbers[left] + numbers[right] > target:
                right -=1
            if left < right and numbers[left] + numbers[right] == target:
                results.append([-target, numbers[left], numbers[right]])
                left += 1
                right -=1


s = Solution()
numbers = [1,0,-1,-1,-1,-1,0,1,1,1]
print(s.threeSum(numbers))
