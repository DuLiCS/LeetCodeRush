//
// Created by DuLi on 2023/10/16.
//
#include<iostream>
using std::vector;
class Solution {
public:
    bool canJump(vector<int>& nums) {
        int max_reach = 0;
        int target = nums.size() - 1;

        for (int i = 0; i < nums.size(); ++i) {
            if (i > max_reach){
                return false;
            }
            max_reach = max_reach > (i + nums[i]) ? max_reach : (i + nums[i]);
            if (max_reach >= target){
                return true;
            }
        }
        return false;
    }
};