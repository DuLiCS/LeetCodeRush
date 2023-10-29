//
// Created by DuLi on 2023/10/29.
//
#include<iostream>
using std::vector;
int canCompleteCircuit(vector<int>& gas, vector<int>& cost) {
    int current_tank = 0;
    int total_tank = 0;
    int station = 0;

    for (int i = 0; i < gas.size(); ++i) {
        current_tank += gas[i] - cost[i];
        total_tank += gas[i] - cost[i];
        if (current_tank < 0){
            current_tank = 0;
            station = i + 1;
        }
    }
    if (total_tank >= 0){
        return station;
    } else{
        return -1;
    }
}
