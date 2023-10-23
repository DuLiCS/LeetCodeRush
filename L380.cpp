//
// Created by DuLi on 2023/10/23.
//

#include "L380.h"
#include <iostream>
#include <unordered_map>
#include<cstdlib>

class RandomizedSet {
private:
    std::vector<int> val_list;
    std::unordered_map<int, int> index_map;

public:
    /** Initialize your data structure here. */
    RandomizedSet() {
    }

    /** Inserts a value to the set. Returns true if the set did not already contain the specified element. */
    bool insert(int val) {
        if (index_map.find(val) == index_map.end()) {
            val_list.push_back(val);
            index_map[val] = val_list.size() - 1;
            return true;
        }
        return false;
    }

    /** Removes a value from the set. Returns true if the set contained the specified element. */
    bool remove(int val) {
        if (index_map.find(val) != index_map.end()) {
            int temp = val_list.back();
            int index = index_map[val];

            val_list[index] = temp;
            index_map[temp] = index;

            val_list.pop_back();
            index_map.erase(val);

            return true;
        }
        return false;
    }

    /** Get a random element from the set. */
    int getRandom() {
        int index = rand() % val_list.size();
        return val_list[index];
    }
};