/*
 * 334. Order Check
 * https://www.lintcode.com/problem/order-check/my-submissions
 */
#include <bits/stdc++.h>
class Solution {
public:
    /**
     * @param heights: Students height
     * @return: How many people are not where they should be
     */
    int orderCheck(vector<int> &heights) {
        // write your code here
        vector<int> sortedHeights(heights);
        sort(sortedHeights.begin(), sortedHeights.end());
        int count = 0;
        for (int i = 0; i < heights.size(); ++i) {
            if (heights[i] != sortedHeights[i]) count++;
        }
        return count;
    }
};
