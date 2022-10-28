#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    bool isPalindrome(int x) {
        if (x < 0) {
            return false;
        }
        if (x == 0) { // to avoid log10(0)
            return true;
        }
        int digits = (int)log10(x) + 1; // compute -> x digits
        int times = digits / 2; // we need to compare n / 2 times (move two pointers at one move)
        int left = (int)pow(10, digits - 1), right = 1;
        while (times--) {
            if ((x / left) % 10 != (x / right) % 10) { // if (left digit != right digit)
                return false;
            }
            left /= 10;
            right *= 10;
        }
        return true;
    }
};
