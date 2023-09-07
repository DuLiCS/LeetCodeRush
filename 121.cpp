//
// Created by DuLi on 2023/9/7.
//
#include <iostream>
using std::vector;

class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int max_profit = 0;
        int min_price = prices[0];

        for (int price : prices){
            if (price < min_price){
                min_price = price;
            }
            else if (max_profit < price - min_price){
                max_profit = price - min_price;
            }
        }
        return max_profit;
    }
};