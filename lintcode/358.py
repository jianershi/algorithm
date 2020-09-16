"""
358. treePlanning
https://www.lintcode.com/problem/treeplanning/my-submissions
"""
class Solution:
    """
    @param trees: the positions of trees.
    @param d: the minimum beautiful interval.
    @return: the minimum number of trees to remove to make trees beautiful.
    """
    def treePlanning(self, trees, d):
        # write your code here.
        last_tree = []
        counter = 0
        for t in trees:
            if len(last_tree) == 0:
                last_tree.append(t)
                continue
            if last_tree and t - last_tree[-1] < d:
                counter += 1
                continue
            last_tree.append(t)
        return counter