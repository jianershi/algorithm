/**
 * B. Negative Prefixes
 * https://codeforces.com/contest/1418/problem/B
 *
 * solution:
 * use max heap to sort position that were not locked.
 * fill them from big -> small
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
vector<int> calPrefixSum(vector<int>& arr) {
    vector<int> prefixSum(arr.size(), 0);
    prefixSum[0] = arr[0];
    for (int i = 1; i < arr.size(); ++i) {                  
       prefixSum[i] = prefixSum[i - 1] + arr[i];
    }
    return prefixSum;
}

 void solve() {
     int n; cin >> n;
     vector<int> arr;
     vector<int> locked;
     vector<int> heap;
     for (int i = 0; i < n; ++i) {
         int a; cin >> a;
         arr.push_back(a);
    }
    for (int i = 0; i < n; ++i) {
        int a; cin >> a;
        locked.push_back(a);
    }

    debug(arr, locked);
    vector<int> prefixSum = calPrefixSum(arr);
    debug(prefixSum);

    for (int i = 0; i < n; ++i) {
        if (locked[i]) continue;
        heap.push_back(arr[i]);
    }
    make_heap(heap.begin(), heap.end());

    for (int i = 0; i < n; ++i) {
        if (locked[i]) continue;
        pop_heap(heap.begin(), heap.end());
        arr[i] = heap.back();
        heap.pop_back();
    }

    debug(arr, calPrefixSum(arr));
    for (int i = 0; i < arr.size(); ++i){
        cout << arr[i] << (i < arr.size() - 1 ? " " : "");
    }
    cout << endl;
}



int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);
    // freopen("input.txt", "r", stdin);
    // freopen("output.txt", "w", stdout);

    int tc; cin >> tc;
    for (int t = 1; t <= tc; t++) {
        // cout << "Case #" << t  << ": ";
        solve();
    }
}
