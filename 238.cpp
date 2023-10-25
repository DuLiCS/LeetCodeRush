//
// Created by DuLi on 2023/10/25.
//
#include<iostream>
using std::vector;

vector<int> productExceptSelf(vector<int>& nums) {
    int n = nums.size();
    vector<int> ans(n, 1);
    int left = 1;
    for (int i = 1; i < n; ++i) {
        left *= nums[i - 1];
        ans[i] *= left;
    }
    int right = 1;
    for (int i = n - 2; i > -1; --i) {
        right *= nums[i + 1];
        ans[i] *= right;
    }
    return ans;
}