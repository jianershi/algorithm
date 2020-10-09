"""
a<=b<=c
a+b+c = 0 => b+c = -a


"""
class Solution:
    """
    @param numbers: Give an array numbers of n integer
    @return: Find all unique triplets in the array which gives the sum of zero.
    """
    def threeSum(self, numbers):
        # write your code here
        if not numbers:
            return []
        n = len(numbers)
        
        numbers = sorted(numbers)
        result = set()
        for i in range(n):
            self.two_sum(-numbers[i], numbers, i + 1, result)
        
        return [list(x) for x in result]
        
    def two_sum(self, target, numbers, starting_index, result):
        v = set()
        n = len(numbers)
        for i in range(starting_index, n):
            if target - numbers[i] in v:
                result.add((-target, target - numbers[i], numbers[i]))
            v.add(numbers[i])
            
        