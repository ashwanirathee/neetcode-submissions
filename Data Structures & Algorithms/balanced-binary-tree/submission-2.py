# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        h_r = self.maxHeight(root.left)
        h_l = self.maxHeight(root.right)
        height_diff = abs(h_r - h_l)
        if height_diff <= 1:
            return True and self.isBalanced(root.right) and self.isBalanced(root.left)
        else:
            return False

    def maxHeight(self, root):
        if not root: return 0
        return max(self.maxHeight(root.left), self.maxHeight(root.right)) + 1