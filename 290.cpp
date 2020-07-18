/*
290. Sorted Arrangement
https://www.lintcode.com/problem/sorted-arrangement/description
周赛题. segment tree
O(nlogn)
*/
// #import <bits/stdc++.h>
#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

class MySegmentTreeNode {
public:
    int start, end, sum;
    MySegmentTreeNode *left, *right;

    MySegmentTreeNode(int start, int end) {
        this->start = start;
        this->end = end;
        this->sum = 0;
        this->left = this->right = NULL;
    }
};

class Solution {
private:
    MySegmentTreeNode* build(int start, int end) {
        if (start > end) {
            return NULL;
        }
        if (start == end) {
            return new MySegmentTreeNode(start, end);
        }
        
        MySegmentTreeNode* node = new MySegmentTreeNode(start, end);
        
        int mid = (start + end) / 2;
        node->left = build(start, mid);
        node->right = build(mid + 1, end);

        return node;
    }
    
    void modify(MySegmentTreeNode* root, int index, int value) {
        if (root->start == index && root->end == index) {
            root->sum = value;
            return;
        }

        int mid = (root->start + root->end) / 2;
        if (root->start <= index && index <= mid) {
            modify(root->left, index, value);
        }

        if (mid + 1 <= index and index <= root->end) {
            modify(root->right, index, value);
        }

        root->sum = root->left->sum + root->right->sum;
    }

    int query(MySegmentTreeNode* root, int start, int end) {
        if (start == root->start and end == root->end) {
            return root->sum;
        }

        int mid = (root->start + root->end) / 2;

        int left_sum = 0, right_sum = 0;

        if (start <= mid) {
            if (mid < end) {
                left_sum = query(root->left, start, mid);
            } else {
                left_sum = query(root->left, start, end);
            } 
        }

        if (mid + 1 <= end) {
            if (start <= mid) {
                right_sum = query(root->right, mid + 1, end);
            } else {
                right_sum = query(root->right, start, end);
            }
        }

        return left_sum + right_sum;
    }
public:
    /**
     * @param nums: the array of elements to be inserted.
     * @return: return the least operation number.
     */
    long long sortedArrangement(vector<int> &nums) {
        // write your code here
        int n = nums.size();
        if (n == 0) {
            return 0;
        }
        long long max_move = 0;
        
        MySegmentTreeNode *root = build(0, 1e5 +1);
        
        for (int i = 0; i < n; ++i){
            int left_move = query(root, 0, nums[i]);
            int right_move = query(root, nums[i] + 1, 1e5);

            max_move += min(left_move, right_move) * 2 + 1;
            cout << "left: " << left_move << " right: " << right_move << " moves: " << max_move << " nums[i]: " << nums[i] << endl;
            modify(root, nums[i], 1);
        }
        return max_move;
    }

};

int main() {
    Solution s;
    vector<int> nums{1,3,2,4};
    cout << s.sortedArrangement(nums) << endl;
}