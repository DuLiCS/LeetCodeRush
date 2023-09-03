//
// Created by DuLi on 2023/9/3.
//

#include <iostream>
using std::vector;

class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int p1 = 0;

        for (int i = 1; i < nums.size(); ++i) {
            if (nums[i] != nums[p1]){
                p1++;
                nums[p1] = nums[i];
            }
        }
        return p1 + 1;
    }
};