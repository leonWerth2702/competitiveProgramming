#include <bits/stdc++.h>
#define ll long long
using namespace std;
 
void solve()
{
    int n;
    cin >> n;
    vector<int> arr(n);
    string s;
 
    for (int i = 0; i < n; i++)
        cin >> arr[i];
    cin >> s;
 
    for (int i = 0; i < n - 1; i++)
    {
        for (int j = i + 1; j < n; j++)
        {
            if (arr[i] == arr[j] && s[i] != s[j])
            {
                cout << "NO\n";
                return;
            }
        }
    }
    cout << "YES\n";
}
 
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int t;
    cin >> t;
    while (t--)
    {
        solve();
    }
}
