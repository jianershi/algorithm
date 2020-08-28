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
            int min_index = n;
            for (int k = j + 1; k < n; ++k) {
                if (interval_list[k].first[0] >= interval_list[j].first[1]) {
                    min_index = interval_list[k].second;
                    break;
                }
            }
            res[interval_list[j].second] = min_index == n ? -1 : min_index;
        }
        return res;

    }
};
