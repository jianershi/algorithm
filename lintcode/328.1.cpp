/**
328. String Partition
https://www.lintcode.com/problem/string-partition/my-submissions
other people's solution
1. find index
2. expand right bracket as needed
3. when right bracket = index <- good bound <-within this range all chars have been accoutned for
4. insert res
**/
class Solution {
public:
    /**
     * @param s: a string
     * @return:  an array containing the length of each part
     */
    vector<int> splitString(string &s) {
        // write your code here.
        unordered_map<char, int> last_index;
        for (int i = 0; i < s.size(); ++i) {
            last_index[s[i]] = i;
        }
        vector<int> res;
        int l = 0, r = 0;
        for (int i = 0; i < s.size(); ++i) {
            r = max(r, last_index[s[i]]);
            if (r == i) {// at last index, good bound 
                res.emplace_back(r - l + 1);
                l = r + 1;
            }
        }
        return res;
    }
};