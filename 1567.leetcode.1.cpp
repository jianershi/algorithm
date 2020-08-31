/**
1567. Maximum Length of Subarray With Positive Product
https://leetcode.com/problems/maximum-length-of-subarray-with-positive-product/
slightly modified solution for readability based on 
https://leetcode.com/problems/maximum-length-of-subarray-with-positive-product/discuss/819278/Java-O(n)-time-O(1)-space
**/
class Solution {
public:
    int getMaxLen(vector<int>& nums) {
        int max_len = 0, first_neg = -1, zero_i = - 1, neg = 0, n = nums.size();
        for (int i = 0; i < n; ++i) {
            if (nums[i] == 0) {
                neg = 0, first_neg = -1; zero_i = i;
            } else if (nums[i] < 0) {
                neg++;
                if (first_neg == -1) first_neg = i;
            } 
            
            if (neg % 2 == 0) max_len = max(max_len, i - zero_i);
            else max_len = max(max_len, i - first_neg);
        }
        
        return max_len;
    }
};