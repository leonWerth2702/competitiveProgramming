#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int> &nums, int target) {
        map<int, int> map;
        vector<int> ans;
        int complement = 0;
        for (int i = 0; i < nums.size(); ++i) {
            complement = target - nums[i];
            if (map.find(complement) != map.end()) {
               ans.push_back(i);
               ans.push_back(map.find(complement)->second);
               return ans;
            }
            map.insert({nums[i], i});
        }
        return ans;
    }
};
