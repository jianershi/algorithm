/**
143. Reorder List
https://leetcode.com/problems/reorder-list/
**/
#include <vector>
#include <iostream>
using namespace std;
// struct ListNode {
//       int val;
//       ListNode *next;
//       ListNode() : val(0), next(nullptr) {}
//       ListNode(int x) : val(x), next(nullptr) {}
//       ListNode(int x, ListNode *next) : val(x), next(next) {}
// };
 
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

class Solution {
public:
    void reorderList(ListNode* head) {
        ListNode* root = head;
        vector<ListNode*> stack;
        ListNode* node = head;
        while (node) {
            stack.push_back(node);
            node = node->next;
        }

        int n = stack.size() / 2;
        for (int i = 0; i < n; ++i) {
            node = stack.back(); stack.pop_back();
            node->next = head->next;
            head->next = node;
            head = node->next;
        }

        if (head) head->next = nullptr;
    }
};