#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    int findMinLength(vector<string> &strs) {
        int minLen = (int) strs[0].length();
        for (int i = 1; i < strs.size(); ++i) {
            minLen = min(minLen, (int) strs[i].length());
        }
        return minLen;
    }

    string longestCommonPrefix(vector<string> &strs) {
        if (strs.empty()) {
            return "";
        }
        string ans;
        int minLen = findMinLength(strs);
        for (int i = 0; i < minLen; ++i) {
            char current = strs[0][i];
            for (int j = 1; j < strs.size(); ++j) {
                if (strs[j][i] != current) {
                    return ans;
                }
            }
            ans.push_back(current);
        }
        return ans;
    }
};
