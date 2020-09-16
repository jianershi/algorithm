/**
317. Minimum Parentheses Matching
https://www.lintcode.com/problem/minimum-parentheses-matching/description

公式答案
**/
#include <iostream>
#include <deque>
using namespace std;
class Solution{
  public:
    string minimumParenthesesMatching(string s){
        std::deque<int> star_st;
        int l = 0, r = 0;
        for (int i = 0; i < s.size(); ++i) {
            if (s[i] == '(') {
                ++l;
            } else if (s[i] == ')') {
                ++r;
                if (r > l) {
                    if (star_st.empty()) {
                        return "No solution!";
                    }
                    int ind = star_st.front();
                    star_st.pop_front();
                    s[ind] = '(';
                    l += 1;
                }
            } else {
                star_st.push_back(i);
            }
        }
        
        star_st.clear();
        l = 0, r = 0;
        for (int i = s.size() - 1; ~i; --i) {
            if (s[i] == '(') {
                ++l;
                if (l > r) {
                    if (star_st.empty()) {
                        return "No solution!";
                    }
                    int ind = star_st.front();
                    star_st.pop_front();
                    s[ind] = ')';
                    r += 1;
                }
            } else if (s[i] == ')') {
                ++r;
            } else {
                star_st.push_back(i);
            }
        }
        
        s.erase(remove(s.begin(), s.end(), '*'), s.end()); //https://en.wikipedia.org/wiki/Erase%E2%80%93remove_idiom
        return s;
    }
};

int main() {
    Solution s;
    string str = "((***)()((**";
    cout << s.minimumParenthesesMatching(str) << endl;
}