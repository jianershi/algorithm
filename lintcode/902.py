"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the given BST
    @param k: the given k
    @return: the kth smallest element in BST
    """
    def kthSmallest(self, root, k):
        # write your code here
        k_index, smallest_k = self.find_kth_smallest_index(root, 0, k)
        return smallest_k
            
    """
    @param root: current node
    @param target_k: target 
    @return current_index
    @return smallest_k if already otherwise None
    直接用in-order traversal
    分治法：如果左子树已经找到了，就返回左子树的结果，如果没有，就+1 然后看等不等于k, 如果等于就返回本颗子树，如果右边子树已经找到了就返回右边子树找到的结果。假如都没有，就返回右边子树的index因为inorder traversal右边子树返回的index才是当前已经搜索过的个数。这个方法因为遍历了所有的点，所以时间复杂度O(N).
    更好的方法是用lower bound, upper bound, 时间复杂度是O(h), 因为只需要找2次树的高度就够了。（https://www.jiuzhang.com/solution/closest-binary-search-tree-value/#tag-highlight-lang-java）
    """
    def find_kth_smallest_index(self, root, current_index, target_index):
        if root is None:
            return current_index, None
            
        k_index_left, smallest_k_left = self.find_kth_smallest_index(root.left, current_index, target_index)
        if k_index_left == target_index:
            return k_index_left, smallest_k_left

        current_index = k_index_left + 1
        if current_index == target_index:
            return current_index, root.val
            
        k_index_right, smallest_k_right = self.find_kth_smallest_index(root.right, current_index, target_index)
        if k_index_right == target_index:
            return k_index_right, smallest_k_right
        
        return k_index_right, smallest_k_right