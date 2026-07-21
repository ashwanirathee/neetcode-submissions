# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = [root]
        result = []
        while queue:
            print("nw")
            res = []
            curr_res = []
            for i in queue:
                curr = i
                # print(curr.val)
                curr_res.append(curr.val)
                if i.left: res.append(i.left)
                if i.right: res.append(i.right)
            queue = []
            queue.extend(res)
            result.append(curr_res)

        for i in range(len(result)):
            if i % 2 == 1:
                result[i] = reversed(result[i])

        return result