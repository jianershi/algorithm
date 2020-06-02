"""
645. Find the Celebrity

brute force

time compexity o(n^2)

"""
"""
The knows API is already defined for you.
@param a, person a
@param b, person b
@return a boolean, whether a knows b
you can call Celebrity.knows(a, b)
"""


class Solution:
    # @param {int} n a party with n people
    # @return {int} the celebrity's label or -1
    def findCelebrity(self, n):
        # Write your code here
        if not n or n == 0:
            return -1

        for candidate in range(n):
            is_celebrity = True
            for i in range(n):
                if i == candidate:
                    continue
                if not Celebrity.knows(i, candidate) or Celebrity.knows(candidate, i):
                    is_celebrity = False
                    break
            if is_celebrity:
                return candidate
        return -1
