/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */

class Solution {
public:
    vector<vector<int>> levelOrder(TreeNode* root) {
        if(root == NULL) return {};
        queue<TreeNode*> listing;
        listing.push(root);
        vector<vector<int>> test;
        while(!listing.empty()){
            vector<int> v1;
            int count = listing.size();
            for(int i=0;i<count;i++){
                TreeNode* node = listing.front();
                std::cout << node->val << std::endl;
                listing.pop();
                v1.push_back(node->val);
                if(node->left != NULL) listing.push(node->left);
                if(node->right != NULL) listing.push(node->right);
            }
            test.push_back(v1);

        }
        return test;
    }
};
