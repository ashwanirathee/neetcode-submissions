# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.data = []

        def dfs(root):
            if not root: return None
            dfs(root.left)
            self.data.append(root.val)
            dfs(root.right)

        dfs(root)
        print(self.data)
        self.idx = 0

    def next(self) -> int:
        self.idx +=1
        return self.data[self.idx-1]

    def hasNext(self) -> bool:
        if len(self.data) > self.idx:
            return True
        else:
            return False
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()