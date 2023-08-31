//
// Created by DuLi on 2023/8/31.
//

#include <iostream>
using std::string;

class Solution {
public:
    string reverseVowels(string s) {
        string vowels = "aeiouAEIOU";
        int left = 0;
        int right = s.size() - 1;

        while (left < right) {
            while (left < right && vowels.find(s[left]) == string::npos) {
                left++;
            }
            while (left < right && vowels.find(s[right]) == string::npos) {
                right--;
            }
            std::swap(s[left], s[right]);
            left++;
            right--;
        }

        return s;
    }

public:
    std::string reverseVowels_stack(std::string s) {
        string vowels = "aeiouAEIOU";

        std::vector<char> stack;
        for (char c : s) {
            if (vowels.find(c) != string::npos){
                stack.push_back(c);
            }
        }

        string result = "";
        for (char c : s){
            if (vowels.find(c) != string::npos){
                result += stack.back();
                stack.pop_back();
            }
            else{
                result += c;
            }
        }
        return result;
    }
};

int main(){
        Solution sol;
        string s = "leetcode";
        std::cout << sol.reverseVowels_stack(s);

        return 0;
};
