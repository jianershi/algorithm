/**
436. Find Right Interval
https://leetcode.com/problems/find-right-interval/
easier implementation
**/
class Solution {
public:
    vector<int> findRightInterval(vector<vector<int>>& intervals) {
        vector<pair<int, int>> l;
        int n = intervals.size();
        vector<int> res(n);
        for (int i = 0; i < n; ++i) {
            l.push_back(make_pair(intervals[i].front(), i));
        }
        sort(l.begin(), l.end());

        for (int j = 0; j < n; ++j) {
            auto r = lower_bound(l.begin(), l.end(), make_pair(intervals[j].back(), 0));
            res[j] = r != l.end() ? r->second : - 1;
        }
        return res;

    }
};
