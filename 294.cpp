/*
294. Linked List Simplification

https://www.lintcode.com/problem/linked-list-simplification/description?_from=contest&&fromId=96
*/
/**
 * Definition of singly-linked-list:
 * class ListNode {
 * public:
 *     int val;
 *     ListNode *next;
 *     ListNode(int val) {
 *        this->val = val;
 *        this->next = NULL;
 *     }
 * }
 */
#include <iostream>
#include <string>
using namespace std;

class ListNode {
 public:
      int val;
      ListNode *next;
      ListNode(int val) {
         this->val = val;
         this->next = NULL;
      }
};
class Solution {
public:
    /**
     * @param head: the linked list to be simplify.
     * @return: return the linked list after simplifiction.
     */
    ListNode * simplify(ListNode * head) {
        // write your code here
        if (head == NULL) {
            ListNode *root = new ListNode(0);
            return root;
        }
        ListNode* root = head;
        int count = -2;
        ListNode* tail = head;
        ListNode* prev = new ListNode(0);
        while (tail) {
            ++count;
            prev = tail;
            tail = tail->next;
        }
        
        tail = root;
        string s = to_string(count);

        for (int i = 0; i < s.size(); ++i) {
            tail->next = new ListNode(s[i]);
            tail = tail->next;
        }
        tail->next = prev;
        return root;
    }
};

int main() {
    ListNode *root = new ListNode('h');
    ListNode *tail = root; 
    tail->next = new ListNode('e'); tail = tail->next;
    tail->next = new ListNode('l'); tail = tail->next;
    tail->next = new ListNode('l'); tail = tail->next;
    tail->next = new ListNode('o'); tail = tail->next;
    Solution s;
    s.simplify(root);

    tail = root;
    while (tail != NULL) {
      cout << tail->val << endl;
      tail = tail->next;
    }

}