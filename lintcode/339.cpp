/*
 * 339. Median II
 * https://www.lintcode.com/problem/median-ii/description?_from=contest&&fromId=105
 */
#include <bits/stdc++.h>
class Solution {
public:
    /**
     * @param arr: an integer array
     * @return: return the median array when delete a number
     */
    vector<int> getMedian(vector<int> &arr) {
        // write your code here
        vector<int> newArr = arr;
        sort(newArr.begin(), newArr.end());
        int n = arr.size();
        
        int l_c = newArr[n / 2 - 1], r_c = newArr[n / 2];
        vector<int> res(n, 0);
        for (int i = 0; i < n; ++i) {
            if (arr[i] <= l_c) res[i] = r_c;
            if (arr[i] >= r_c) res[i] = l_c;
        }
        return res;
        
    }
};
