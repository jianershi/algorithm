/**
328. String Partition
https://www.lintcode.com/problem/string-partition/my-submissions
1. find all indexes of a unique char
2. build max range of unique char
3. sort range
3. merge range
4. got len of range and return
**/
class Solution {
public:
    /**
     * @param s: a string
     * @return:  an array containing the length of each part
     */
    vector<int> splitString(string &s) {
        // write your code here.
        unordered_map<char, vector<int>> indices;
        for (int i = 0; i < s.size(); ++i) {
            indices[s[i]].push_back(i);
        }
        vector<pair<int, int>> ranges;
        for (auto &c: indices) {
            ranges.push_back(make_pair(*min_element(c.second.begin(), c.second.end()), *max_element(c.second.begin(), c.second.end())));
        }
        sort(ranges.begin(), ranges.end());
        vector<pair<int, int>> combined;
        for (auto &r: ranges) {
            if (combined.empty() || r.first > combined.back().second)
                combined.push_back(r);
            else
                combined.back().second = max(combined.back().second, r.second);
        }
        vector<int> res;
        for (auto &r: combined) {
            res.push_back(r.second - r.first + 1);
        }
        return res;
    }
};
