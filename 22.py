"""
22. Flatten List
https://www.lintcode.com/problem/flatten-list/description
"""
class Solution(object):

    # @param nestedList a list, each element in the list 
    # can be a list or integer, for example [1,2,[1,2]]
    # @return {int[]} a list of integer
    def flatten(self, nestedList):
        # Write your code here
        results = []
        self.dfs(nestedList, 0, results)
        return results

    def dfs(self, curr_list, index, results):
        if curr_list == []:
            return
        if index == len(curr_list):
            results.append(curr_list[:])
            return

        for item in curr_list:
            if type(item) == list:
                self.dfs(item, 0, results)
            else:
                results.append(item)


s = Solution()
nestedList = [[1,1],2,[1,1]]
print(s.flatten(nestedList))