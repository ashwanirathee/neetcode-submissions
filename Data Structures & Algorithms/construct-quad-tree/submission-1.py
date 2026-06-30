"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""


class Solution:
    def construct(self, grid: List[List[int]]) -> "Node":
        n = len(grid)
        # print("Intially:", n)
        if n == 1:
            if grid[0][0] == 1:
                return Node(val=True, isLeaf=True)
            else:
                return Node(val=False, isLeaf=True)

        mid = n // 2

        top_left = self.construct([row[:mid] for row in grid[:mid]])
        top_right = self.construct([row[mid:] for row in grid[:mid]])
        bot_left = self.construct([row[:mid] for row in grid[mid:]])
        bot_right = self.construct([row[mid:] for row in grid[mid:]])

        if (
            top_left.isLeaf
            and top_right.isLeaf
            and bot_left.isLeaf
            and bot_right.isLeaf
            and (top_left.val == top_right.val == bot_left.val == top_left.val == bot_right.val) 
        ):
            return Node(top_right.val, True)
        
        return Node(True, False, top_left, top_right, bot_left, bot_right)

        
