class Solution {
public:
    std::string clean(string s){
        std::string res = "";
        for(auto it: s){
            if(std::isalnum(it)) res += tolower(it);
        }
        return res;
    }
    bool isPalindrome(string s) {
        std::string test = clean(s);
        int l = 0;
        int r = test.size() - 1;
        std::cout << test << std::endl;
        while(l <= r){

            if(test[l] != test[r]) return false;
            std::cout << l << " " << r << " " << test[l] << " " << test[r] << std::endl;
            l++;
            r--;
        }
        
        return true;
    }
};
