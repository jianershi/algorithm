/**
 * A. Subset Mex
 * https://codeforces.com/contest/1406/problem/A
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

void solve() {
    int n;
    cin >> n;
    vector<int> arr;
    int count[101];
    memset(count, 0, sizeof count);
    for (int i = 0 ; i < n; ++i) {
        int x; cin >> x;
        count[x]++;
    }
    int l = 0, r = 0;
    for (int i = 0; i <= 100; ++i){
        if (count[i] == 0) {
            l = i;
            break;
        }
    }
    for (int i = 0; i <= 100; ++i) {
        if (count[i] <= 1) {
            r = i;
            break;
        }
    }
    
    cout << l + r << endl;

}

int main() {
    // ios_base::sync_with_stdio(0);
    // cin.tie(0); cout.tie(0);
    // freopen("input.txt", "r", stdin);
    // freopen("output.txt", "w", stdout);

    int tc; cin >> tc;
    for (int t = 1; t <= tc; t++) {
    // cout << "Case #" << t  << ": ";
    solve();
    }
}
