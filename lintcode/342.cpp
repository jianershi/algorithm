/**
 * 342. Valley sequence
 * https://www.lintcode.com/problem/valley-sequence/leaderboard
 *
 * dp1[i], longest decreasing subsequence ending in i
 * dp2[i], longest increasing subsequence starting from i
 *
 *
 */
#include <bits/stdc++.h>

using namespace std;

#define ar array
#define ll long long

const int MAX_N = 1e5 + 1;
const int MOD = 1e9 + 7;
const int INF = 1e9;
const ll LINF = 1e18;

void __print(int x) {cerr << x;}
void __print(long x) {cerr << x;}
void __print(long long x) {cerr << x;}
void __print(unsigned x) {cerr << x;}
void __print(unsigned long x) {cerr << x;}
void __print(unsigned long long x) {cerr << x;}
void __print(float x) {cerr << x;}
void __print(double x) {cerr << x;}
void __print(long double x) {cerr << x;}
void __print(char x) {cerr << '\'' << x << '\'';}
void __print(const char *x) {cerr << '\"' << x << '\"';}
void __print(const string &x) {cerr << '\"' << x << '\"';}
void __print(bool x) {cerr << (x ? "true" : "false");}

template<typename T, typename V>
void __print(const pair<T, V> &x) {cerr << '{'; __print(x.first); cerr << ','; __print(x.second); cerr << '}';}
template<typename T>
void __print(const T &x) {int f = 0; cerr << '{'; for (auto &i: x) cerr << (f++ ? "," : ""), __print(i); cerr << "}";}
void _print() {cerr << "]\n";}
template <typename T, typename... V>
void _print(T t, V... v) {__print(t); if (sizeof...(v)) cerr << ", "; _print(v...);}
#ifndef ONLINE_JUDGE
#define debug(x...) cerr << "[" << #x << "] = ["; _print(x)
#else
#define debug(x...)
#endif


class Solution {
public:
    /**
     * @param num: sequence
     * @return: The longest valley sequence
     */
    int valley(vector<int> &num) {
        int n = num.size();
        vector<int> dp1(n, 1);
        vector<int> dp2(n, 1);

        for (int i = 0; i < n; ++i) {
            for (int j = 0;j < i; ++j) {
                if (num[j] < num[i])
                    dp1[j] = max(dp1[j], dp1[i] + 1);
            }
        }

        for (int i = n - 2; ~i; --i) {
            for (int j = n - 1; j > i; --j) {
                if (num[i] < num[j])
                    dp2[i] = max(dp2[i], dp2[j] + 1);
            }
        }

        int res = 0;
        for (int i = 0; i < n; ++i) {
            for (int j = 1; j < n; ++j) {
                if (num[i] == num[j]) {
                    res = max(res, min(dp1[i], dp2[j]) * 2);
                }
            }
        }
        return res;
    }
};
