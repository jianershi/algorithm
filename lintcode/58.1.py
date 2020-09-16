"""
58. 4Sum
wrong answer

"""
class Solution:
    """
    @param numbers: Give an array
    @param target: An integer
    @return: Find all unique quadruplets in the array which gives the sum of zero
    """
    def fourSum(self, numbers, target):
        # write your code here
        numbers = sorted(numbers)
        n = len(numbers)
        results = []

        last_pair = (None, None, None, None)
        for i in range(n):
            for j in range(i + 1, n):
                left, right = j + 1, n - 1
                while left < right:
                    while (numbers[i], numbers[j], numbers[left], numbers[right]) == last_pair:
                        left += 1
                        right -= 1
                    while left < right and numbers[left] + numbers[right] < target - numbers[i] - numbers[j]:
                        left += 1
                    while left < right and numbers[left] + numbers[right] > target - numbers[i] - numbers[j]:
                        right -= 1
                    if left < right and numbers[left] + numbers[right] == target - numbers[i] - numbers[j]:
                        candidate = [numbers[i], numbers[j], numbers[left], numbers[right]]
                        results.append(candidate)
                        last_pair = tuple(candidate)
                        left += 1
                        right -= 1

        return results

s = Solution()
numbers = [1,0,-1,-1,-1,-1,0,1,1,1,2]
print (sorted(numbers))

target = 2
print(s.fourSum(numbers, target))
