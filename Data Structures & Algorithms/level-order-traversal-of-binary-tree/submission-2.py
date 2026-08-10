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
        queue = deque([root])
        output = []
        while queue:
            nq = deque([])
            res = []
            for i in queue:
                curr = i
                res.append(curr.val)
                if curr.left: nq.append(curr.left)
                if curr.right: nq.append(curr.right)
            output.append(res)
            queue = deque(nq)
        return output