/**
 * E. Expected Damage
 * https://codeforces.com/contest/1418/problem/E
 *
 * using Modular Multiplicative Inverse
 * https://cp-algorithms.com/algebra/module-inverse.html
 *
 */
#include <bits/stdc++.h>

using namespace std;

#define ar array
#define ll long long

const int MAX_N = 1e5 + 1;
const int MOD = 998244353;
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
long long fastPower(long long a, long long n) {
    a %= MOD;
    long long ans = 1;
    while (n > 0) {
        if (n & 1) 
            ans = ans * a % MOD;
        a = a * a % MOD;
        n >>= 1;
    }
    return ans;
}

vector<int> calPrefixSum(vector<int> &d) {
    int n = d.size();
    vector<int> prefixSum(n + 1);
    for (int i = 1; i < n + 1; ++i) {
        prefixSum[i] = (prefixSum[i - 1] % MOD + d[i - 1] % MOD) % MOD;
    }
    return prefixSum;
}


void process(int durability, int defenseRating, vector<int> &damage, vector<int> &prefixSum) {
    int n = damage.size();
        
    int index = lower_bound(damage.begin(), damage.end(), defenseRating) - damage.begin();
    int bigMonster = n - index;
    long long sumSmall = prefixSum[index] % MOD;
    long long sumBig = (prefixSum[n] - prefixSum[index] + MOD) % MOD; //aditional MOD need to be added, because during prefix calculation, later prefix could be smaller, but at most MOD difference, this makes sure the result is always positive
    int s = max(0, bigMonster + 1 - durability);
    int b = max(0, bigMonster - durability);
    int totalDamage = (1LL * sumSmall * s % MOD * fastPower(bigMonster + 1, MOD - 2) % MOD + 1LL * sumBig * b % MOD * fastPower(bigMonster, MOD - 2) % MOD) % MOD;  

    debug(damage, prefixSum, durability, defenseRating);
    cout << totalDamage << endl;
}

void solve() {
    int n, m; cin >> n >> m;
    vector<int> d;
    for (int i = 0; i < n; ++i) {
        long long a; cin >> a;
        d.push_back(a);
    }
    sort(d.begin(), d.end());
    vector<int> prefixSum = calPrefixSum(d);
    for (int i = 0; i < m; ++i) {
        int a, b; cin >> a >> b;
        process(a, b, d, prefixSum);
    }
}

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);
    // freopen("input.txt", "r", stdin);
    // freopen("output.txt", "w", stdout);

   // int tc; cin >> tc;
 //   for (int t = 1; t <= tc; t++) {
        // cout << "Case #" << t  << ": ";
        solve();
   // }
}
