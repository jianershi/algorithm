class Solution:
    """
    @param numbers: An array of Integer
    @param target: target = numbers[index1] + numbers[index2]
    @return: [index1 + 1, index2 + 1] (index1 < index2)
    """
    def twoSum(self, numbers, target):
        # write your code here
        numbers = [(v, i) for (i,v) in enumerate(numbers)]
        numbers = sorted(numbers)
        n = len(numbers)
        l, r = 0, n - 1
        while l < r:
            while l < r and numbers[l][0] + numbers[r][0] < target:
                l += 1
            while l < r and numbers[l][0] + numbers[r][0] > target:
                r -= 1
            if l < r and numbers[l][0] + numbers[r][0] == target:
                return sorted([numbers[l][1], numbers[r][1]])
        return [-1, -1]