/**
 * 104. Merge K Sorted Lists
 * https://www.lintcode.com/problem/merge-k-sorted-lists/description
 * suppose k list, total member count of all list N
 * 方法3，从下往上，2，2归并
 * 2,2 合并O(N)
 * 数的高度logK
 * 所以O(Nlogk)
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
        
        vector<ListNode *> currentList = lists;
        
        while (currentList.size() > 1) {
            vector<ListNode *> nextList;
            for (int i = 0; i < currentList.size(); i += 2) {
                if (i == currentList.size() - 1) {
                    nextList.push_back(currentList[i]);
                    continue;
                }
                nextList.push_back(merge2list(currentList[i], currentList[i + 1]));
            }
            currentList = nextList;
        }
        return currentList[0];
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


