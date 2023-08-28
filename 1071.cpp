//
// Created by DuLi on 2023/8/28.
//
#include <iostream>
using std::string;

class Solution1071 {
public:
    string gcdOfStrings(string str1, string str2) {
        string lstr, sstr;
        lstr = str1.size() >= str2.size() ? str1 : str2;
        sstr = str1.size() < str2.size() ? str1 : str2;

        if (lstr.size() % sstr.size() == 0){
            if (lstr == repeatString(sstr, lstr.size() / sstr.size())){
                return sstr;
            }
        }

        for (int i = 1;i<sstr.size();++i) {
            string divisor = sstr.substr(0, sstr.size() - i);
            if (lstr.size() % divisor.size() == 0 && sstr.size() % divisor.size() == 0) {
                if (sstr == repeatString(divisor, sstr.size() / divisor.size()) && (lstr == repeatString(divisor, lstr.size()/divisor.size()))){
                    return divisor;
                }
            }
        }

        return "";
    }

private:
    static std::string repeatString(const std::string& str, int times) {
        std::string result;
        for (int i = 0; i < times; ++i) {
            result += str;
        }
        return result;
    }

};

class Solution1071Recusion {
public:
    string gcdOfStrings(string str1, string str2) {
        if (str1.empty() || str2.empty()){
            return str1.empty() ? str2 : str1;
        }
        if (str1 + str2 != str2 + str1){
            return "";
        }
        if (str1.substr(0, str2.size()) == str2){
            return this->gcdOfStrings(str1.substr(str2.size()), str2);
        }
        if (str2.substr(0, str1.size()) == str1){
            return this->gcdOfStrings(str1, str2.substr(str1.size()));
        }

        return "";
    }
};

int main(){
    Solution1071 sol;
    string str1 = "NLZGMNLZGMNLZGMNLZGMNLZGMNLZGMNLZGMNLZGM";
    string str2 = "NLZGMNLZGMNLZGMNLZGMNLZGMNLZGMNLZGMNLZGMNLZGM";
    string result = sol.gcdOfStrings(str1, str2);

    string str3 = "ABCABC";
    string str4 = "ABC";
    Solution1071Recusion solr;
    result = solr.gcdOfStrings(str3, str4);
    std::cout<<result;
}