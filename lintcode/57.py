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

        numbers = sorted(numbers)
        # print (numbers)
        results = []
        index = 0
        last_number = None
        while index < len(numbers):
            if last_number is not None and numbers[index] == last_number:
                index += 1
                continue
            self.two_sum(numbers, index + 1, -numbers[index], results)
            last_number = numbers[index]
            index += 1

        return results

    def two_sum(self, numbers, starting_index, target, results):
        # print (index, target)
        map = set()
        last_number = None
        for i in range(starting_index, len(numbers)):
            if last_number is not None and numbers[i] == last_number:
                continue
            if target - numbers[i] in map:
                results.append([-target, target - numbers[i], numbers[i]])
                last_number = numbers[i]
            map.add(numbers[i])


s = Solution()
numbers = [0,0,0,0]
print(s.threeSum(numbers))
