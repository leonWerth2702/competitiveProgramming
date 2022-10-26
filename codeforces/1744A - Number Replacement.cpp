#include <bits/stdc++.h>

using namespace std;

void solve() {
    int n;
    cin >> n;
    vector<int> arr(n);
    string s;
    for (int i = 0; i < n; ++i) {
        cin >> arr[i];
    }
    cin >> s;

    for (int i = 0; i < n - 1; ++i) {
        for (int j = i + 1; j < n; ++j) {
            if (arr[i] == arr[j] && s[i] != s[j]) {
                cout << "NO" << endl;
                return;
            }
        }
    }
    cout << "YES" << endl;
}

int main() {
    int numberOfTestCase;
    cin >> numberOfTestCase;
    while (numberOfTestCase--) {
        solve();
    }
}
