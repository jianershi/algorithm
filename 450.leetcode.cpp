/**
 * 450. Delete Node in a BST
 * https://leetcode.com/problems/delete-node-in-a-bst/submissions/
 *
 * algorithm:
 * http://www.algolist.net/Data_structures/Binary_search_tree/Removal
 */
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    TreeNode* deleteNode(TreeNode* root, int key) {
        if (!root) return nullptr;
        if (key == root->val) {
            root = remove(root);
        } else if (key < root->val) {
            root->left = deleteNode(root->left, key);
        } else {
            root->right = deleteNode(root->right, key);
        }
        return root;
    }
    
    TreeNode* remove(TreeNode* root) {
        TreeNode *l = root->left;
        TreeNode *r = root->right;
        if (!l) return root->right;
        if (!r) return root->left;
        //have both left and right child, find minimum node in the right subtree
        TreeNode *node = r;
        while (node->left)
            node = node->left;
        root->val = node->val;
        root->right = deleteNode(root->right, node->val);
        return root;
    }
};