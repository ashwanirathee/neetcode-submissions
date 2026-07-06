# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if len(inorder) == 0 or len(postorder) == 0:
            return None

        root_val = postorder[-1]
        # print(inorder, postorder)
        idx = 0
        n = len(inorder)
        for i in range(n):
            if inorder[i] == root_val:
                idx = i
                break

        root = TreeNode(inorder[idx])
        root.left = self.buildTree(inorder[:idx], postorder[:idx])
        root.right = self.buildTree(inorder[idx+1:], postorder[idx:-1]) 

        return root