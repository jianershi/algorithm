/**
86. Binary Search Tree Iterator
https://www.lintcode.com/problem/binary-search-tree-iterator/description
**/

/**
 * Definition of TreeNode:
 * class TreeNode {
 * public:
 *     int val;
 *     TreeNode *left, *right;
 *     TreeNode(int val) {
 *         this->val = val;
 *         this->left = this->right = NULL;
 *     }
 * }
 * Example of iterate a tree:
 * BSTIterator iterator = BSTIterator(root);
 * while (iterator.hasNext()) {
 *    TreeNode * node = iterator.next();
 *    do something for node
 */
class BSTIterator {
private: 
    std::stack<TreeNode *> stack;
    
public:
    /*
    * @param root: The root of binary tree.
    */BSTIterator(TreeNode * root) {
        // do intialization if necessary
        TreeNode *p = root;
        while (p != NULL) {
            stack.push(p);
            p = p->left;
        }
    }

    /*
     * @return: True if there has next node, or false
     */
    bool hasNext() {
        // write your code here
        return stack.size() > 0;
    }

    /*
     * @return: return next node
     */
    TreeNode * next() {
        // write your code here
        TreeNode* node = stack.top();
        if (node->right) {
            TreeNode* n = node->right;
            while (n) {
                stack.push(n);
                n = n->left;
            }
        }
        else {
            TreeNode* n = stack.top();
            stack.pop();
            while (stack.size() > 0 and stack.top()->right == n) {
                n = stack.top();
                stack.pop();
            }
        }
        
        return node;
    }
};