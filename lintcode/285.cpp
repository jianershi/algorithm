/**
285. Tall Building
https://www.lintcode.com/problem/tall-building/description
monotonic stack
**/
class Solution {
public:
    /**
     * @param arr: the height of all buildings
     * @return: how many buildings can he see at the location of each building
     */
    vector<int> tallBuilding(vector<int> &arr) {
        // Write your code here.
        int n = arr.size();

        vector<int> pre = buildPre(arr);

        vector<int> revarr(arr.rbegin(), arr.rend());
        vector<int> after = buildPre(revarr);

        vector<int> res;
        for (int i = 0; i < n; ++i) {
            res.push_back(pre[i] + 1 + after[n - 1 - i]);
        }
        return res;
    }

    vector<int> buildPre(vector<int>& arr) {
        int n = arr.size();
        vector<int> stack;
        vector<int> res;
        for (int i = 0; i < n; ++i) {
            res.push_back(stack.size());
            while (!stack.empty() && arr[i] >= stack.back()) {
                stack.pop_back();
            }
            stack.push_back(arr[i]);
        }
        return res;
    }
};
