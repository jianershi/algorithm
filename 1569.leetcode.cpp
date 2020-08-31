/**
1569. Number of Ways to Reorder Array to Get Same BST
https://leetcode.com/contest/weekly-contest-204/problems/number-of-ways-to-reorder-array-to-get-same-bst/
brute force
TLE
**/
class MyTreeNode {
public:
    MyTreeNode *left = nullptr, *right = nullptr;
    int val;
    MyTreeNode(int val): val(val) {}
    
    static MyTreeNode* buildTree(vector<int>& nums) {
        MyTreeNode *root = new MyTreeNode(nums[0]);
        for (int i = 1; i < nums.size(); ++i) {
            root->insert(nums[i]);
        }
        return root;
    }
    
    void insert(int num) {
        if (num < this->val) {
            if (!left) left = new MyTreeNode(num);
            else left->insert(num);
        } else {
            if (!right) right = new MyTreeNode(num);
            else right->insert(num);
        }
    }
    
    static bool compareTree(MyTreeNode *t1, MyTreeNode *t2) {
        if (t1 == nullptr && t2 == nullptr) return true;
        if (t1 == nullptr) return false;
        if (t2 == nullptr) return false;
        if (t1->val != t2->val) return false;
        return compareTree(t1->left, t2->left) && compareTree(t1->right, t2->right);
    }
};

class Solution {
private:
    int count;
public:
    int numOfWays(vector<int>& nums) {
        MyTreeNode *root = MyTreeNode::buildTree(nums);
        vector<int> path;
        dfs(nums, path, root);
        return count - 1;
    }
    
    void dfs(vector<int>& nums, vector<int>& path, MyTreeNode *ot) {
        if (path.size() == nums.size()) {
            MyTreeNode *root = MyTreeNode::buildTree(path);
            if (MyTreeNode::compareTree(root, ot)) count++;
            return;
        }
        
        for (int i = 0; i < nums.size(); ++i) {
            if (find(path.begin(), path.end(), nums[i]) != path.end()) continue;
            path.push_back(nums[i]);
            dfs(nums,path,ot);
            path.pop_back();
        }
    }
    
    
};