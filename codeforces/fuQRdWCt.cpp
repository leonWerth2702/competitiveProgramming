#include <bits/stdc++.h>

using namespace std;

void solve() {
    string s;
    cin >> s;
    int n = (int)s.length();
    int k = 7;

    for (int i = 0; i <= n - k; ++i) {
        int cnt = 0;
        for (int j = i; j <= i + k - 1; ++j) {
            if (s[i] == s[j]) {
                cnt++;
            }
        }
        if (cnt == 7) {
            cout << "YES" << endl;
            return;
        }
    }
    cout << "NO" << endl;
}

int main() {
    solve();
    return 0;
}
