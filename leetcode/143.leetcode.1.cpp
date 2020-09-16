/**
143. Reorder List
https://leetcode.com/problems/reorder-list/
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
            end = slow;
            slow = slow->next;
        }
        
        end->next = nullptr;
        
        ListNode *secondRoot = reverseLinkedList(slow);
        mergeTwoLinkedList(head, secondRoot);
    }
    
    ListNode* reverseLinkedList(ListNode* head) {
        ListNode *prev = nullptr, *n;
        while (head) {
            n = head->next;
            head->next = prev;
            prev = head;
            head = n;
        }
        return prev;
    }
    
    void mergeTwoLinkedList(ListNode* a, ListNode* b) {
        ListNode *prev, *tail;
        while (a && b) {
            tail = a->next;
            a->next = b;
            prev = b;
            b = b->next;
            a->next->next = tail;
            a = tail;
        }
        
        if (!a) {
            prev->next = b;
        }
    }
    
};