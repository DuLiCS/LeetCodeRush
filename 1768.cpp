//
// Created by DuLi on 2023/8/26.
//
#include <iostream>
using namespace std;

class Solution{
public:
    string mergeAlternately(string word1, string word2) {
        string result;
        int i;
        for (i = 0; i < min(word1.size(),word2.size()); ++i) {
            result += word1[i];
            result += word2[i];
        }

        if (word1.size() != word2.size()){
            return result += (word1.size() > word2.size()) ? word1.substr(i): word2.substr(i);
        }
        return result;
    }
};

int main(){
    Solution sol;
    string word1 = "abcdef";
    string word2 = "pqr";
    string result;
    result = sol.mergeAlternately(word1, word2);
    cout<<result;
}

