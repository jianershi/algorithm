"""
1836. Reaching Point
Example 1:
Input:
start = [1, 1]
target = [5, 2]
Output: True
Explanation: (1, 1) -> (1, 2) -> (3, 2) -> (5, 2)

solution
"""
class Solution:
    """
    @param start: a point [x, y]
    @param target: a point [x, y]
    @return: return True or False
    """
    def ReachingPoints(self, start, target):
        while start[0] <= target[0] and start[1] <= target[1]:
            if start == target:
                return True
            if target[0] < target[1]:
                target = [target[0], target[1] - target[0]]
            else:
                target = [target[0] - target[1], target[1]]
        return False

s = Solution()
start = [1, 2]
target =[99840,40832]
print(s.ReachingPoints(start, target))
