/**
 * 1578. Minimum Deletion Cost to Avoid Repeating Letters
 * https://leetcode.com/contest/weekly-contest-205/problems/minimum-deletion-cost-to-avoid-repeating-letters/
 * https://leetcode.com/problems/minimum-deletion-cost-to-avoid-repeating-letters/discuss/831588/JavaC%2B%2BPython-Straight-Forward
 */
class Solution {
public:
    int minCost(string s, vector<int>& cost) {
        int n = s.size(), res = 0, rangeCost = 0, rangeMax = 0;
        for (int i = 0; i < n; ++i) {
            if (i > 0 && s[i] != s[i - 1]) {
                res += rangeCost - rangeMax;
                rangeCost = rangeMax = 0;
            }
            rangeCost += cost[i];
            rangeMax = max(rangeMax, cost[i]);
        }
        res += rangeCost - rangeMax;
        return res;
    }
};