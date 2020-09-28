/**
 * C. Santa's Bot
 * https://codeforces.com/group/tKC7z9Nm0A/contest/295533/problem/C
 *
 * probability = 1/n * 1/n * Σ(for all presents) total occurrence of x among all gift list / total length of gift list which includes x
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
            ans = (ans * a) % MOD;
        a = (a * a) % MOD;
        n >>= 1;
    }
    return ans;
}

long long inv(long long x) {
    return fastPower(x, MOD - 2);
}

void solve() {
    long long n; cin >> n;
    vector<long long> presents(1e6, 0);
    vector<long long> totalPresents(1e6, 0);

    for (long long i = 0; i < n; ++i) {
        long long k; cin >> k;
        for (long long  j = 0; j < k; ++j) {
            long long p; cin >> p;
            presents[p]++;
            totalPresents[p] = (totalPresents[p] + inv(k)) % MOD;
        }
    }
   
    long long sumOfPresentProbability = 0;
    for (long long i = 0; i <= 1e6; ++i) {
        sumOfPresentProbability = (sumOfPresentProbability + presents[i] * totalPresents[i] % MOD) % MOD;
    }
    
    long long res = inv(n) * inv(n) % MOD * sumOfPresentProbability % MOD;

    debug(sumOfPresentProbability, res);
    cout << res << endl;
}

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);
    // freopen("input.txt", "r", stdin);
    // freopen("output.txt", "w", stdout);

 //   int tc; cin >> tc;
//    for (int t = 1; t <= tc; t++) {
        // cout << "Case #" << t  << ": ";
        solve();
//    }
}
