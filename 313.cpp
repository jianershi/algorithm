/**
313. Minimum Insertion
https://www.lintcode.com/problem/minimum-insertion/description

u can take either the first or the last element and insert into anywhere in the string.
ffff|xxxxx|bbbb
x x x x x x x x <- relative position doesn't change while f, and b will have relative position changed
->find a substring in a so that it is the longest subsequence of b? some what similar problem. 
what happens if found? how to get minimum movement if found such sequence?

公式答案
**/
#include <vector>
#include <iostream>
#include <unordered_map>
using namespace std;
class Solution {
public:
    /**
     * @param a: the array you need to operate.
     * @param b: the target array.
     * @return: return the minimum number of operations.
     */
    int minimumInsertion(vector<int> &a, vector<int> &b)
    {
        unordered_map<int, int> map;
        int max_len = 1;
        int curr_len = 1;
        for (int i = 0; i < b.size(); ++i) {
            map[b[i]] = i;
        }
        for (int i = 1; i < a.size(); ++i) {
            if (map[a[i]] > map[a[i - 1]]) {
                curr_len += 1;
                max_len = max(max_len, curr_len);
            }
            else {
                curr_len = 1;
            }
        }
        return b.size() - max_len;
    }
};

int main(){
    Solution s;
    vector<int> a = {5,4,1,3,2};
    vector<int> b = {1,2,3,4,5};
    cout << s.minimumInsertion(a, b) << endl;
}