/**
 * D. Trash Problem
 * https://codeforces.com/contest/1418/problem/D
 * TLE
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

vector<int> calPrefixSum(vector<int> &arr) {
    int n = arr.size();
    vector<int> prefixSum(n + 1, 0);
    for (int i = 1; i < n + 1; ++i) {
        prefixSum[i] = prefixSum[i - 1] + arr[i - 1];
    }
    return prefixSum;
}

void cal(vector<int> &arr) {
    vector<int> diff;
    for (int i = 1; i < arr.size(); ++i) {
        diff.push_back(arr[i] - arr[i - 1]);
    }
    vector<int> prefixSum = calPrefixSum(diff);
    vector<int> revDiff(diff.rbegin(), diff.rend());
    vector<int> reversePrefixSum = calPrefixSum(revDiff);
    reverse(reversePrefixSum.begin(), reversePrefixSum.end());

    prefixSum.insert(prefixSum.begin(), 0);
    reversePrefixSum.emplace_back(0);

    int min_step = INT_MAX;
    for (int i = 0; i < prefixSum.size(); ++i) {
        min_step = min(min_step, prefixSum[i] + reversePrefixSum[i]);
    }
    debug(min_step);
    cout << min_step << endl;

}

void solve() {
    int n, q; cin >> n >> q;
    vector<int> arr;
    for (int i = 0; i < n; ++i) {
        int a; cin >> a;
        arr.push_back(a);
    }
    sort(arr.begin(), arr.end());
    cal(arr);
    for (int i = 0; i < q; ++i) {
        int t, pos;
        cin >> t >> pos;
        auto it = lower_bound(arr.begin(), arr.end(), pos);
        if (t == 0) arr.erase(it);
        if (t == 1) arr.insert(it, pos);
        cal(arr);
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
