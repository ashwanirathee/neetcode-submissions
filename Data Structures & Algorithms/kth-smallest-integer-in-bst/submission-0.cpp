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
    vector<int> data;
    void solve(TreeNode* root){
        if(root == NULL) return;
        solve(root->left);
        data.push_back(root->val);
        std::cout << root->val << std::endl;
        solve(root->right);
    }
    int kthSmallest(TreeNode* root, int k) {
        solve(root);
        return data[k-1];
    }
};
