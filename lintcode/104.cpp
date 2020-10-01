/**
 * 104. Merge K Sorted Lists
 * https://www.lintcode.com/problem/merge-k-sorted-lists/description
 * suppose k list, total member count of all list N
 * o(k) for creating the heap
 * each time pop and insert o(logk)
 * and have to do it of total N times
 * o(k + Nlogk)
 * using heap
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
private:
static bool cmp(const ListNode * const a , const ListNode * const b) {
    return a->val > b->val;
}
public:
    /**
     * @param lists: a list of ListNode
     * @return: The head of one sorted list.
     */
    
    ListNode *mergeKLists(vector<ListNode *> &lists) {
        // write your code here
        vector<ListNode *> heap;
        for (auto& l: lists) {
            if (l)
                heap.push_back(l);
        }
        make_heap(heap.begin(), heap.end(), cmp);
        ListNode *dummy = new ListNode(0);
        ListNode *tail = dummy;
        while(!heap.empty()) {
            pop_heap(heap.begin(), heap.end(), cmp);
            ListNode *head = heap.back(); heap.pop_back();
            tail->next = head;
            tail = head;
            if (head->next) {
                heap.push_back(head->next);
                push_heap(heap.begin(), heap.end(), cmp);
            }
            
        }
        return dummy->next;
    }
};


