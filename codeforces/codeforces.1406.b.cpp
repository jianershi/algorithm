/**
 * B. Maximum Product
 * https://codeforces.com/contest/1406/problem/B
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
    int n; cin >> n;
    vector<int> arr;
    for (int i = 0; i < n; ++i) {
        int a; cin >> a;
        arr.push_back(a);
    }
    long long ans = 1;
    sort(arr.begin(),arr.end(),[&](auto& a, auto&b){return abs(a) > abs(b);});
    if (*max_element(arr.begin(), arr.end()) < 0) {
        for (int i = n - 1; i > n - 6; --i) {
            ans *= arr[i];
        }
        cout << ans << endl;
        return;
    }

    ans = 1;
    for (int i = 0; i < 5; ++i) {
        ans *= arr[i];
    }
    
    if (ans >= 0) {
        cout << ans << endl;
        return;
    }

    for (int i = 5; i < arr.size(); ++i){
        for (int j = 0; j < 5; ++j) {
            long long tmp = arr[i];
            for (int k = 0; k < 5; ++k) {
                if (j != k ) {
                    tmp *= arr[k];
                }
            }
        ans = max(ans, tmp);
        }
    }
    cout << ans << endl;
    return;
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
