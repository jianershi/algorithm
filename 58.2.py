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

        for i in range(n):
            if i > 0 and numbers[i] == numbers[i - 1]:
                continue
            for j in range(i + 1, n):
                if j > i + 1 and numbers[j] == numbers[j - 1]:
                    continue

                left, right = j + 1, n - 1
                last_pair = (None, None)
                while left < right:
                    while (numbers[left], numbers[right]) == last_pair:
                        left += 1
                        right -= 1
                    while left < right and numbers[left] + numbers[right] < target - numbers[i] - numbers[j]:
                        left += 1
                    while left < right and numbers[left] + numbers[right] > target - numbers[i] - numbers[j]:
                        right -= 1
                    if left < right and numbers[left] + numbers[right] == target - numbers[i] - numbers[j]:
                        candidate = [numbers[i], numbers[j], numbers[left], numbers[right]]
                        results.append(candidate)
                        last_pair = (numbers[left], numbers[right])
                        left += 1
                        right -= 1

        return results


s = Solution()
numbers = [1,0,-1,-1,-1,-1,0,1,1,1,2]
target = 2
print(s.fourSum(numbers, target))
