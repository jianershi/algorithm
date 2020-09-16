/**
 * 969. Pancake Sorting
 * https://leetcode.com/problems/pancake-sorting/submissions/
 * 
 * bubble sort
 *
 * using reverse [a,b)
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
            reverse(arr.begin(), arr.begin() + curr_idx + 1);
            reverse(arr.begin(), arr.begin() + t);
            res.push_back(curr_idx + 1);
            res.push_back(t);
        }
        return res;
    }
};