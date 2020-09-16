/**
143. Reorder List
https://leetcode.com/problems/reorder-list/
official solution
**/
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
        if (!head or !head->next) return;
        ListNode *fast = head, *slow = head, *end;
        
        while (fast && fast->next) {
            fast = fast->next->next;
            slow = slow->next;
        }
        
        ListNode *secondRoot = reverseLinkedList(slow);
        mergeTwoLinkedList(head, secondRoot);
    }
    
    ListNode* reverseLinkedList(ListNode* head) {
        ListNode *prev = nullptr, *curr = head;
        while (curr) {
            ListNode *n = curr->next;
            curr->next = prev;
            prev = curr;
            curr = n;
        }
        return prev;
    }
    
    void mergeTwoLinkedList(ListNode* first, ListNode* second) {
        while (second->next) {
            ListNode *tmp = first->next;
            first->next = second;
            first = tmp;
            
            tmp = second->next;
            second->next = first;
            second = tmp;
        }
    }
    
};