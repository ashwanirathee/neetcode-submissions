# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
        def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
            if root == None:
                return 0
            depth_right = self.maxHeight(root.right)
            depth_left = self.maxHeight(root.left)
            diameter = depth_right + depth_left
            return max(diameter, self.diameterOfBinaryTree(root.right), self.diameterOfBinaryTree(root.left))
            
        def maxHeight(self, root: Optional[TreeNode]) -> int:
            if root == None:
                return 0
            return max(self.maxHeight(root.right), self.maxHeight(root.left)) + 1