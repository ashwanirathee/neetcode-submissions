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
    int width = 0;
    int solve(TreeNode* root, int depth){
        if(root == NULL) return 0;        
        int l = solve(root->left, depth + 1);
        std::cout << root->val << " " << depth <<std::endl;
        int r = solve(root->right, depth + 1);
        width = max(width, l + r);
        std::cout << "l:" << l << " " << "r:" << r << std::endl;
        return max(l,r) + 1;
    }
    int diameterOfBinaryTree(TreeNode* root) {
        int res = solve(root, 0);
        return width;
    }
};
