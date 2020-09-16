/**
 * D. Trash Problem
 * https://codeforces.com/contest/1418/problem/D
 *
 * answer on website
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

// xl   x    xr
void insert(int a, set<int> &x, multiset<int> &diff) {
    x.insert(a);
    auto it = x.find(a);
    if (it != x.begin() && next(it) != x.end()) {
        diff.erase(diff.find(*next(it) - *prev(it)));
    }
    if (it != x.begin()) {
        diff.insert(a - *prev(it));
    }
    if (next(it) != x.end()) {
        diff.insert(*next(it) - a);
    }
}

void remove(int a, set<int> &x, multiset<int> &diff) {
    auto it = x.find(a);
    if (it != x.begin() && next(it) != x.end()) {
        diff.insert(*next(it) - *prev(it));
    }
    if (next(it) != x.end())
        diff.erase(diff.find(*next(it) - a));
    if (it != x.begin())
        diff.erase(diff.find(a - *prev(it)));
    x.erase(it);
}

void cal(set<int> &x, multiset<int> &diff) {
    //int res = *max_element(x.begin(), x.end()) - *min_element(x.begin(), x.end()) - *max_element(diff.begin(), diff.end());
    if (x.size() <= 2) { cout << 0 << endl; return; }
    int res = *prev(x.end()) - *x.begin() - *prev(diff.end());
    debug(res);
    cout << res << endl;
}

void solve() {
    int n, q; cin >> n >> q;
    set<int> x;
    multiset<int> diff;
    for (int i = 0; i < n; ++i) {
        int a; cin >> a;
        insert(a, x, diff);
    }
    cal(x, diff);

    for (int i = 0; i < q; ++i) {
        int t, pos;
        cin >> t >> pos;
        if (t == 0) remove(pos, x, diff);
        if (t == 1) insert(pos, x, diff);
        cal(x, diff);
    }
}

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);
    // freopen("input.txt", "r", stdin);
    // freopen("output.txt", "w", stdout);

    //int tc; cin >> tc;
    //for (int t = 1; t <= tc; t++) {
        // cout << "Case #" << t  << ": ";
        solve();
    //}
}
