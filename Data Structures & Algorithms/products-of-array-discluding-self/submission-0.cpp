class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int siz = nums.size();
        vector<int> result(siz, 1);
        int prefix = 1;
        for(int i=0;i< siz;i++){
            result[i] = result[i] * prefix;
            prefix = prefix * nums[i];
            std::cout << prefix << std::endl;
        }

        int postfix = 1;
        for(int i=siz-1;i>=0;i--){
            result[i] = result[i] * postfix;
            postfix = postfix * nums[i];
            std::cout << postfix << std::endl;
        }
        return result;
    }
};
