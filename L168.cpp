//
// Created by DuLi on 2023/9/5.
//
#include<iostream>
using std::vector;

class Solution {
public:
    int majorityElement(vector<int>& nums) {
        int flag = nums[0];
        int cnt = 0;
        for (int num : nums) {
            if (num == flag){
                cnt++;
            } else{
                cnt--;
                if (cnt == 0){
                    flag = num;
                    cnt = 1;
                }
            }
        }
        return flag;
    }
};