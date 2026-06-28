# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        if not root:
            return res
        queue = [[root]]

        while queue:
            print("New level")
            curr_level = queue[0]
            queue.pop(0)

            now = []
            res_curr = []
            for i in curr_level:
                # print(i.val)
                res_curr.append(i.val)


                
                if i.left: now.append(i.left)
                if i.right: now.append(i.right)

            if len(now) > 0:
                queue.append(now) 

            res.append(res_curr)
        return res
            
