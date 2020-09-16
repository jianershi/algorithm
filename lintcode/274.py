"""
274. Make binary tree average
https://www.lintcode.com/problem/make-binary-tree-average/description
九章高频题班。看goodnotes
"""
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
import sys
class Solution:
    """
    @param root: the root
    @return: return the min steps
    """
    def makeBinaryTreeAverage(self, root):
        # write your code here
        dp = {}
        self.dfs(root, dp) #dp{node:({values:cost to change node to values}, max_cost to change root to any number, min_cost to change the tree to any legal tree)}
        return dp[root][2]

    def dfs(self, root, dp):
        if not root:
            return
        
        self.dfs(root.left, dp)
        self.dfs(root.right, dp)

        self.get_dp(root, dp)

    def get_dp(self, root, dp):
        if not root.left and not root.right:
            dp[root] = ({root.val: 0}, 1, 0)
            return

        if not root.left:
            root_map = {}
            right_map = dp[root.right][0]
            min_cost = sys.maxsize #min_cost to make this tree legal

            for value in right_map: # to change right subtree
                if value == root.val:
                    root_map[value] = right_map[value]
                else:
                    root_map[value] = right_map[value] + 1
                min_cost = min(min_cost, root_map[value])

            max_cost = dp[root.right][1] + 1 #cost to change right subtree node to any value

            dp[root] = root_map, max_cost, min_cost
            return

        if not root.right:
            root_map = {}
            left_map = dp[root.left][0]
            min_cost = sys.maxsize

            for value in left_map: # to change current node
                if value == root.val:
                    root_map[value] = left_map[value]
                else:
                    root_map[value] = left_map[value] + 1
                min_cost = min(min_cost, root_map[value])

            max_cost = dp[root.left][1] + 1

            dp[root] = root_map, max_cost, min_cost
            return

        left_map, left_max_cost, left_min_cost = dp[root.left]
        right_map, right_max_cost, right_min_cost  = dp[root.right]

        """
        the change a node to any number, only need
        1) to change left OR right tree to any value
        2) to change right OR left tree to legal tree
        +1 (to change itself to match)
        """
        max_cost = min(left_max_cost + right_min_cost, left_min_cost + right_max_cost) + 1
        root_map = {}
        min_cost = sys.maxsize
        """
        cost of changing root to average of left and right subtree
        """
        for left_value in left_map:
            for right_value in right_map:
                average = (left_value + right_value) / 2
                total_cost = left_map[left_value] + right_map[right_value]
                
                if average != root.val:
                    total_cost += 1

                if total_cost >= max_cost:
                    continue

                root_map[average] = min(root_map.get(average, sys.maxsize), total_cost)
                min_cost = min(min_cost, root_map[average])

        #compare to the cost of not changing root, (change either left or right)
        root_map[root.val] = min(root_map.get(root.val, sys.maxsize), max_cost - 1) # - 1 is for not chaning root.
        min_cost = min(min_cost, root_map[root.val])

        dp[root] = root_map, max_cost, min_cost
        
        return

