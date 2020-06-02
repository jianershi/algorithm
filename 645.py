"""
645. Find the Celebrity

using the solution discussed in class.

o(n) time complexity
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

        candidate = 0
        for i in range(n):
            # if Celebrity.knows(i, candidate):
                # pass
            if not Celebrity.knows(i, candidate):
                candidate = i

        for i in range(n):
            if i == candidate:
                continue
            if not Celebrity.knows(i, candidate) or Celebrity.knows(candidate, i):
                return -1
        return candidate
