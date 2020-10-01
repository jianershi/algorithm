/**
 * 104. Merge K Sorted Lists
 * https://www.lintcode.com/problem/merge-k-sorted-lists/description
 * suppose k list, total member count of all list N
 * using merge sort
 * sort each layer o(N)
 * tree height o(logK)
 * total o(NlogK)
 */
/**
 * Definition of ListNode
 * class ListNode {
 * public:
 *     int val;
 *     ListNode *next;
 *     ListNode(int val) {
 *         this->val = val;
 *         this->next = NULL;
 *     }
 * }
 */
class Solution {
public:
    /**
     * @param lists: a list of ListNode
     * @return: The head of one sorted list.
     */
    
    ListNode *mergeKLists(vector<ListNode *> &lists) {
        if (lists.empty()) return nullptr;
        return mergeSort(0, lists.size() - 1, lists);
    }
    
    ListNode* mergeSort(int start, int end, vector<ListNode* > &lists) {
        if (start == end)
            return lists[start];
        int mid = start + (end - start) / 2;
        ListNode *left = mergeSort(start, mid, lists);
        ListNode *right = mergeSort(mid + 1, end, lists);
        return merge2list(left, right);
    }
    
    ListNode* merge2list(ListNode *left, ListNode *right) {
        ListNode *dummy = new ListNode(0);
        ListNode* tail = dummy;
        while (left && right) {
            if (left->val < right->val) {
                tail->next = left;
                left = left->next;
            }
            else {
                tail->next = right;
                right = right->next;
            }
            tail = tail->next;
        }
        
        if (left) tail->next = left;
        if (right) tail->next = right;
        
        return dummy->next;
    }
};


