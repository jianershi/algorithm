"""
dynamic programming definition:
f[i] = length of Largest Divisible Subset upto X[i]

state expression
f[i] = max(f[j] for j in range 0~-i-1 which are f[i]'s factors and in the dictionary) + 1
f{} is definied as a hash map because it needs to record value and length
so that for X[i], it does not need to iterate over all j, but only X[i]'s
factors
->
better state expression:
f[i] = max(f[j] for all f[i]'s factors which are in the original array) + 1

we can optimize finding factors to O(sqrt(n))

prev record it's path
return the path
"""
import sys
class Solution:
    """
    @param: nums: a set of distinct positive integers
    @return: the largest subset
    """
    def largestDivisibleSubset(self, nums):
        # write your code here
        nums.sort()

        #initialization
        n = len(nums)
        f = {} #{val: length}
        prev = {} #{val: prev_val}

        #all numbers can have factor of itself, so it at least have length 1
        for num in nums:
            f[num] = 1
            prev[num] = None

        #dp according to the definition
        for num in nums:
            for factor in self.get_factors(num):
                if factor not in f:
                    continue
                if f[num] < f[factor] + 1:
                    f[num] = f[factor] + 1
                    prev[num] = factor

        last_val, longest_length = self.get_longest_lsi_length(f)

        path = self.get_path(last_val, prev)

        return path

    """
    efficient way to get a list of factors of num
    @param: num, integer
    @return: factors do not include itself
    """
    def get_factors(self, num):
        factors = []
        j = 1
        while j * j <= num:
            if num % j == 0 and j != num:
                factors.append(j)
                the_other_factor = num // j
                if the_other_factor != num and the_other_factor != j:
                    factors.append(the_other_factor)
            j += 1
        return factors

    def get_longest_lsi_length(self, f):
        last_val, longest_length = None, -1
        for val, length in f.items():
            if length > longest_length:
                last_val = val
                longest_length = length
        return (last_val, longest_length)

    def get_path(self, last_val, prev):
        path = [last_val]
        while prev[last_val] in prev:
            last_val = prev[last_val]
            path.append(last_val)
        return path[::-1]

def main():
    s= Solution()
    nums = [2,3,5,7,11,13,17,19,23,31,1000000007]
    # nums = [1, 2]
    print ("nums: %s" % nums)
    path = s.largestDivisibleSubset(nums)
    print ("path: %s" % path)


if __name__ == "__main__":
    main()
