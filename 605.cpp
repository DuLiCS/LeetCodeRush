//
// Created by DuLi on 2023/8/30.
//
#include <iostream>
using std::vector;

class Solution {
public:
    bool canPlaceFlowers(vector<int>& flowerbed, int n) {
        int count = 0;
        flowerbed.insert(flowerbed.begin(), 0);
        flowerbed.push_back(0);

        for (int i = 1; i < flowerbed.size() - 1; ++i) {
            if (flowerbed[i-1] == 0 && flowerbed[i] == 0 && flowerbed[i+1] == 0){                flowerbed[i] = 1;
                count += 1;
                if (count >= n){
                    return true;
                }
            }
        }
        return false;
    }
};

int main(){
    vector<int> flowerbed = {1, 0, 1, 0, 1, 0, 0, 0, 0};
    int n = 2;
    Solution sol;
    std::cout << sol.canPlaceFlowers(flowerbed, n);

    return 0;
}
