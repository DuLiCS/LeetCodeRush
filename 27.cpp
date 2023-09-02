//
// Created by DuLi on 2023/9/2.
//
#include <iostream>
using std::vector;

class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int k = 0;
        for (int i = 0; i < nums.size(); ++i) {
            if (nums[i] != val){
                nums[k] = nums[i];
                k++;
            }
        }
        return k;
    }
};

int main(){
    Solution sol;
    vector<int> nums = {3, 2, 2, 3};
    int val = 2;
    int result = sol.removeElement(nums, val);
    std::cout << result;
}