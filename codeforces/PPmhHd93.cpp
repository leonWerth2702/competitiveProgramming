#include <bits/stdc++.h>

using namespace std;

void solve() {
    string s;
    cin >> s;
    int cnt = 1;
    for (int i = 1; i < s.length(); ++i) {
        if (s[i] == s[i - 1]) {
            cnt++;
            if (cnt == 7) {
                cout << "YES" << endl;
                return;
            }
        } else {
            cnt = 1;
        }
    }
    cout << "NO" << endl;
}

int main() {
    solve();
    return 0;
}
