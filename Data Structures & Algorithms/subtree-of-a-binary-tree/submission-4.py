# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def same_tree(root, subRoot):
            if root and not subRoot:
                return False

            if not root and subRoot:
                return False

            if not root and not subRoot:
                return True
            return root.val == subRoot.val and same_tree(root.left, subRoot.left) and same_tree(root.right, subRoot.right)

        if not root:
            return False
        
        if same_tree(root, subRoot):
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)