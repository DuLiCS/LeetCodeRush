//
// Created by DuLi on 2023/10/17.
//
#include <iostream>
using std::vector;

class Solution {
public:
    int jump(vector<int>& nums) {
        int farthest = 0;
        int end = 0;
        int steps = 0;

        for (int i = 0; i < nums.size() - 1; ++i) {
            farthest = farthest > nums[i] + i ? farthest : nums[i] + i;
            if (i == end){
                steps ++;
                end = farthest;
            }
        }
        return steps;
    }
};