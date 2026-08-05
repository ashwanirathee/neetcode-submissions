# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        inf = float("inf")
        q = deque([(root, -inf, inf)])
        while q:
            root, left, right = q.popleft()
            if not (left < root.val < right):
                return False
            else:
                if root.left: q.append((root.left, left, root.val))
                if root.right: q.append((root.right, root.val, right))
        return True