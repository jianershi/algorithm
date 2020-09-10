/**
 * 1159. Longest Common Prefix III
 * https://www.lintcode.com/problem/longest-common-prefix-iii/description
 * brute force
 */
class Solution {
public:
    /**
     * @param arr: string array
     * @param query: query array
     * @return: return  LCP ans array
     */
    int LCP(string a, string b) {
        for (int i = 0; i < a.size() && i < b.size(); ++i) {
            if (a[i] != b[i]) return i;
        }
        return min(a.size(), b.size());
    }
    vector<int> queryLCP(vector<string> &arr, vector<vector<int>> &query) {
        // write your code here
        map<pair<int, int>, int> memo;
        vector<int> res;
        for (auto& q: query) {
            if (memo.count(make_pair(q[0],q[1])) != 0)
                res.push_back(memo[make_pair(q[0],q[1])]);
            else if  (memo.count(make_pair(q[1],q[0])) != 0)
                res.push_back(memo[make_pair(q[1],q[0])]);
            else {
                memo[make_pair(q[0],q[1])] = LCP(arr[q[0]], arr[q[1]]);
                res.push_back(memo[make_pair(q[0],q[1])]);
            }
        }
        return res;
    }
};