"""
22. Flatten List
https://www.lintcode.com/problem/flatten-list/description

recursion 2
"""
class Solution(object):

    # @param nestedList a list, each element in the list 
    # can be a list or integer, for example [1,2,[1,2]]
    # @return {int[]} a list of integer
    def flatten(self, nestedList):
        # Write your code here
        results = []
        for item in nestedList:
            if isinstance(item, int):
                results.append(item)
            else:
                results.extend(self.flatten(item))
        return results