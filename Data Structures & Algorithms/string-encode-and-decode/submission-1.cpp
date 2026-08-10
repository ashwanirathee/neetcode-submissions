class Solution {
public:
    string encode(vector<string>& strs) {
        string s;
        for(auto it: strs){
            s += it;
            s += "-";
        }
        return s;
    }

    vector<string> decode(string s) {
        vector<string> res;
        std::string temp;
        for(int i=0;i<s.size();i++){
            if(s[i] == '-'){
                string ans = temp;
                res.push_back(ans);
                temp = "";
                continue;
            } 
            temp += s[i];
        }
        return res;
    }
};
