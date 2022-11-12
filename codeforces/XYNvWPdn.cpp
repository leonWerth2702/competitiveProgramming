#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    int shortestStr(vector<string> &strs) {
        int minLen = INT_MAX, minIndex = -1;
        for (int i = 0; i < strs.size(); ++i) {
            if (strs[i].length() < minLen) {
                minLen = (int) strs[i].length();
                minIndex = i;
            }
        }
        return minIndex;
    }
    string longestCommonPrefix(vector<string> &strs) {
        if (strs.empty()) {
            return "";
        }
        int shortestStrIndex = shortestStr(strs);
        while (strs[shortestStrIndex].length() > 0) {
            int cnt = 0;
            for (int i = 0; i < strs.size(); ++i) {
                if (strs[i].find(strs[shortestStrIndex]) == 0) {
                    cnt++;
                }
            }
            if (cnt == strs.size()) {
                return strs[shortestStrIndex];
            }
            strs[shortestStrIndex].pop_back();
        }
        return "";
    }
};
