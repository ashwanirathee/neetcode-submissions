"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        def dfs(node):
            if node == None:
                return None

            oldToNew = {}
            if node in oldToNew:
                return oldToNew[node]

            stack = [node]
            visited = set()
            created = Node(node.val)
            oldToNew[node] = created

            while stack:
                curr = stack[-1]
                stack.pop()

                if curr in visited:
                    continue

                visited.add(curr)

                for neighbor in curr.neighbors:
                    if neighbor not in oldToNew:
                        neighbor_new = Node(neighbor.val)
                        oldToNew[neighbor] = neighbor_new

                    oldToNew[curr].neighbors.append(oldToNew[neighbor])

                    if neighbor not in visited:
                        stack.append(neighbor)
                
            return oldToNew[node]

        return dfs(node)