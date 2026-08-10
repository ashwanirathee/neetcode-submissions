class Solution {
public:
    std::vector<std::string> splitString(const std::string& str, char delimiter) {
        std::vector<std::string> tokens;
        std::string token;
        std::stringstream ss(str);

        while (std::getline(ss, token, delimiter)) {
            tokens.push_back(token);
        }

        return tokens;
    }
    string encode(vector<string>& strs) {
        string s;
        for(auto it: strs){
            s += it;
            s += "-";
        }
        return s;
    }

    vector<string> decode(string s) {
        return splitString(s, '-');
    }
};
