#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    int romanToInt(string s) {
        map<char, int> m;
        int ans = 0;
        m.insert({'I', 1});
        m.insert({'V', 5});
        m.insert({'X', 10});
        m.insert({'L', 50});
        m.insert({'C', 100});
        m.insert({'D', 500});
        m.insert({'M', 1000});
        for (int i = 0; i < s.length(); ++i) {
            if (i < s.length() - 1 && m[s[i]] < m[s[i + 1]]) {
                ans = ans + (m[s[i + 1]] - m[s[i]]);
                ++i;
            } else {
                ans += m[s[i]];
            }
        }
        return ans;
    }
};
