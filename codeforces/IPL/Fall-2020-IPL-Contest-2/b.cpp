/**
 * B. Sweets Eating
 * https://codeforces.com/group/tKC7z9Nm0A/contest/295533/problem/B
 *
 * prefix sum
 * a1 a1+a2 a1+a2+a3 a1+a2+a3+a4
 *
 * cost suppose m = 2
 * a1 a1+a2 2a1+a2+a3 2a1+2a2+a3+a4
 * __       ___
 *    _____           _______
 * prefixSum[i] += prefixsum[i - m] starting from m
 */
#include <bits/stdc++.h>

using namespace std;

#define ar array
#define ll long long

const int MAX_N = 1e5 + 1;
const int MOD = 19 + 7;
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
vector<long long> calPrefixSum(vector<int>& arr) {
    int n = arr.size();
    vector<long long> prefixSum(n + 1, 0);
    for (int i = 1; i < n + 1; ++i)
        prefixSum[i] = prefixSum[i - 1] + arr[i - 1];
    return prefixSum;
}

void solve() {
    int n, m; cin >> n >> m;
    vector<int> arr;
    for (int i = 0; i < n; ++i) {
        int a; cin >> a;
        arr.push_back(a);
    }
    sort(arr.begin(), arr.end());
    vector<long long> prefixSum = calPrefixSum(arr);
    for (int i = m + 1; i <= n; ++i) {
        prefixSum[i] += prefixSum[i - m];
    }
    debug(prefixSum);
    for (int i = 1; i <= n; ++i) cout << prefixSum[i] << " "; cout << endl;
}

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);
    // freopen("input.txt", "r", stdin);
    // freopen("output.txt", "w", stdout);

//    int tc; cin >> tc;
//    for (int t = 1; t <= tc; t++) {
        // cout << "Case #" << t  << ": ";
        solve();
 //   }
}
