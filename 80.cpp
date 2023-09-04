//
// Created by DuLi on 2023/9/4.
//
#include <iostream>
using std::vector;

class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        if (nums.size() < 3)
            return nums.size();

        int p = 2;
        for (int i = 2; i < nums.size(); ++i) {
            if (nums[i] != nums[p-2]){
                nums[p] = nums[i];
                p++;
            }
        }
        return p;
    }
};