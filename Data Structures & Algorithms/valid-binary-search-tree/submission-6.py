# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def helper(root, l, r):
            if not root:
                return True

            value = root.val
            if value <= l or value >= r:
                return False
            else:
                return helper(root.left, l, root.val) and helper(root.right,  root.val, r)

        inf = float("inf")
        return helper(root, -inf, inf)