# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = [root]
        o = []
        while queue:
            nq = []
            res = []
            for curr in queue:
                res.append(curr.val)
                if curr.left: nq.append(curr.left)
                if curr.right: nq.append(curr.right)
            o.append(res)
            queue = nq
        return o
