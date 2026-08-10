class Solution {
public:

    string encode(vector<string>& strs) {
        string ans;
        for(auto it:strs) {
            ans+=it;
            ans+="\n";
        }
        std::cout << ans;
        return ans;
    }

    vector<string> decode(string s) {
        vector<string> res;
        string curr = "";
        for(char c: s){
            if(c == '\n'){
                res.push_back(curr);
                curr = "";
            } else {
                curr += c;
            }
            // std::cout << curr << std::endl;
        }
        return res;
    }
};
