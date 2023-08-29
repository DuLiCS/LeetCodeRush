//
// Created by DuLi on 2023/8/29.
//
#include <iostream>
using std::vector;
class Solution {
public:
    vector<bool> kidsWithCandies(vector<int>& candies, int extraCandies) {
        vector<bool> result;
        int maxCandy = 0;
        for (int candy : candies){
            maxCandy = max(candy + extraCandies, candies);
        }
        for (int candy : candies){
            result.push_back(candy + extraCandies >= maxCandy);
        }
        return result
    }
private:
    int max(int t, vector<int> candies){
        int max = candies[0];
        for (int i = 1; i < candies.size(); ++i) {
            if (candies[i] > max){
                max = candies[i];
            }
        }
        return max;
    }
};

int main(){

    Solution sol;
    sol.kidsWithCandies()
}