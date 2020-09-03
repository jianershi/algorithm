/**
 * 969. Pancake Sorting
 * https://leetcode.com/problems/pancake-sorting/submissions/
 *
 * problem doesn't ask for optimal soution, just any working solution.
 * 
 * bubble sort from largest number -> smallest number
 */
class Solution {
public:
    vector<int> pancakeSort(vector<int>& arr) {
        int n = arr.size();
        vector<int> res;
        for (int t = n; t >= 1; --t) {
            int correct_idx = t - 1;
            if (arr[t - 1] == t) continue;

            int curr_idx = find(arr.begin(), arr.end(), t) - arr.begin();
            flip(arr, 0, curr_idx);
            flip(arr, 0, t - 1);
            res.push_back(curr_idx + 1);
            res.push_back(t);
        }
        return res;
    }
    
    void flip(vector<int>& arr, int l, int r) {
        while (l < r) {
            swap(arr[l++], arr[r--]);
        }
    }
};