#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    string commonPrefixUtil(string &str1, string &str2) {
        string result;
        int len = (int) min(str1.length(), str2.length());
        for (int i = 0; i < len; ++i) {
            if (str1[i] != str2[i]) {
                break;
            }
            result += str1[i];
        }
        return result;
    }
    
    string longestCommonPrefix(vector<string> &strs) {
        if (strs.empty()) {
            return "";
        }
        string ans = strs[0];
        for (int i = 1; i < strs.size(); ++i) {
            ans = commonPrefixUtil(ans, strs[i]);
        }
        return ans;
    }
};

// https://leetcode.com/problems/longest-common-prefix/description/
