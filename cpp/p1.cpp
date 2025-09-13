#include <iostream>
#include <unordered_set>

using std::string;

class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        std::unordered_set<char> uset{};
        int i=0, j=0, result=0;
        if(s.length()<=0){
            return 0;
        }
        while(i<s.length()&&j<s.length()){
            if(uset.find(s[j])!=uset.end()){
                uset.erase(s[i]);
                i++;
            } else {
                uset.insert(s[j]);
                j++;
                result = result>j-i?result:j-i;
            }
        }

        return result;

    }
};

int main(int, char**){
    std::cout << "Hello, from leetcode!\n";
}


