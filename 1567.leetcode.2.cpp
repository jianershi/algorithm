/**
 * 1567. Maximum Length of Subarray With Positive Product
 * https://leetcode.com/problems/maximum-length-of-subarray-with-positive-product/
 * using state to track if there is 2 neg numbers, 0-> even appearance of neg numbers 1-> odd apperance of neg numbers
 * 
 * like prefix sum, .......x....i
 *                              ^ 
 *                         ^
 * 1) at i if there were even numbers of neg numbers appeared before, then only need to find the first occurance of even appearance of neg numbers
 * 2) at i               odd                                                                                        odd
 * |__> this will guarantee anything between index x + 1 and i will have even occurance of negative number
 * 
 * reset state and prevStates if 0 appear
 *
 * similar problem LC930, 1371, 1542, 1567
 */
class Solution {
public:
    int getMaxLen(vector<int>& nums) {
        unordered_map<int, int> prevStates = {{0, -1}}; //state, earliest index
        int maxLen = 0, n = nums.size(), state = 0;
        for (int i = 0; i < n; ++i){
            if (nums[i] == 0) {
                state = 0;
                prevStates.clear();
                prevStates[0] = i;
            } else if (nums[i] < 0) {
                state ^= 1;
            }
            
            if (prevStates.count(state)) maxLen = max(maxLen, i - prevStates[state]);
                
            if (!prevStates.count(state)) prevStates[state] = i;
        }
        return maxLen;
    }
};