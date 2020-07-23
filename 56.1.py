class Solution:
    """
    @param numbers: An array of Integer
    @param target: target = numbers[index1] + numbers[index2]
    @return: [index1 + 1, index2 + 1] (index1 < index2)
    """
    def twoSum(self, numbers, target):
        # write your code here
        v = {}
        for i, n in enumerate(numbers):
            if target - n in v:
                return [v[target - n], i]
            v[n] = i
        