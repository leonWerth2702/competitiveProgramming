#include <bits/stdc++.h>

#define MAX_CHARS 256

using namespace std;

class Solution {
public:
    bool isIsomorphic(string s, string t) {
        bool marked[MAX_CHARS] = { false };
        int map[MAX_CHARS];
        memset(map, -1, sizeof(map));

        for (int i = 0; i < s.length(); ++i) {
            if (map[s[i]] == -1) {
                if (marked[t[i]]) {
                    return false;
                }
                marked[t[i]] = true;
                map[s[i]] = (unsigned char) t[i];
            } else {
                if (map[s[i]] != t[i]) {
                    return false;
                }
            }
        }
        return true;
    }
};
