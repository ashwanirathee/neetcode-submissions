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
    bool res = true;
    int traverse(TreeNode* node, int depth){
        if(node == NULL) return 0;
        int left = traverse(node->left, depth+1);
        std::cout << node->val << " " << depth << std::endl;
        int right = traverse(node->right, depth+1);
        std::cout << "Max:" << max(left, right) << std::endl;
        std::cout << "Max diff:" << left - right << std::endl;
        if(abs(left-right)>1) res = false;
        return max(left, right) + 1;
    }
    bool isBalanced(TreeNode* root) {
        traverse(root, 0);
        return res;
    }
};
