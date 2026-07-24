# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        memo = {}
        def dfs(root):

            if not root:
                return 0

            if root in memo:
                return memo[root]

            # rob
            r1, r2, r3, r4 = 0, 0, 0, 0
            if root.left:
                r1 = dfs(root.left.left)
                r2 = dfs(root.left.right)
            if root.right:
                r3 = dfs(root.right.left)
                r4 = dfs(root.right.right)
            rmax = root.val + r1 + r2 + r3 + r4

            s1 = dfs(root.right)
            s2 = dfs(root.left)
            smax = s1 + s2
            memo[root] = max(rmax, smax)
            return memo[root]

        return dfs(root)