/**
436. Find Right Interval
https://leetcode.com/problems/find-right-interval/
https://leetcode.com/problems/find-right-interval/discuss/91819/C%2B%2B-map-solution
impressive solution using sorted map
**/
class Solution {
public:
    vector<int> findRightInterval(vector<vector<int>>& intervals) {
        map<int, int> start_pos;
        int n = intervals.size();
        for (int i = 0; i < n; ++i) {
            start_pos[intervals[i][0]] = i;
        }
        vector<int> res;
        for (auto& interval: intervals) {
            auto it = start_pos.lower_bound(interval[1]);
            res.push_back(it == start_pos.end() ? -1: it->second);
        }
        return res;
    }
};
