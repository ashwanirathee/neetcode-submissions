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
    bool solve(TreeNode* root, int minval, int maxval){
        if(root == NULL) return true;
        if(root->val <= minval || root->val >= maxval) return false;
        bool l = solve(root->left, minval, min(maxval,root->val));
        bool r = solve(root->right, max(minval, root->val), maxval);
        return l && r;
    }
    bool isValidBST(TreeNode* root) {
        return solve(root, INT_MIN, INT_MAX);;
    }
};
