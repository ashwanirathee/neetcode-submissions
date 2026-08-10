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
    int count = 0;
    void solve(TreeNode* root, int maxv){
        if(root == NULL) return;
        int newmax = max(maxv, root->val);
        if (root->val >= newmax) count++;
        solve(root->left, newmax);
        solve(root->right, newmax);
    }
    int goodNodes(TreeNode* root) {
        solve(root, root->val);
        return count;
    }
};
