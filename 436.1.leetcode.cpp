/**
436. Find Right Interval
https://leetcode.com/problems/find-right-interval/
**/
class Solution {
public:
    vector<int> findRightInterval(vector<vector<int>>& intervals) {
        vector<pair<vector<int>, int>> interval_list;
        int n = intervals.size();
        vector<int> res(n);
        for (int i = 0; i < n; ++i) {
            interval_list.push_back(make_pair(intervals[i], i));
        }
        sort(interval_list.begin(), interval_list.end());

        for (int j = 0; j < n; ++j) {
            int min_insert = lower_bound(interval_list.begin() + j + 1, interval_list.end(), make_pair(vector<int>({interval_list[j].first[1], interval_list[j].first[1]}), 0)) - interval_list.begin();
            int min_index = min_insert == n ? -1 : interval_list[min_insert].second;
            res[interval_list[j].second] = min_index;
        }
        return res;

    }
};
