//
// Created by DuLi on 2023/10/18.
//
#include<iostream>
using std::vector;

int hIndex(vector<int>& citations) {
    int n = citations.size();
    vector<int> buckets(n + 1, 0);

    for (int cite:citations) {
        if (cite > n){
            buckets[n] ++;
        }
        else
        {
            buckets[cite] ++;
        }
    }
        int sum = 0;
        for (int i = n; i >= 0 ; --i) {
            sum += buckets[i];
            if (sum >= i){
                return i;
            }
        }
}

int main(){
    vector<int> citations = {3,0,6,1,5};
    int i = hIndex(citations);
}