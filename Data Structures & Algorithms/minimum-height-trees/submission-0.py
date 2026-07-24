class Solution:
    def getHeight(self, n: int, adj_list: List[List[int]], root: int) -> int:
        visited = set()
        visited.add(root)
        queue = [root]
        height = 1
        while queue:
            queue_size = len(queue)
            new_queue = []
            for node in queue:
                for target in adj_list[node]:
                    if target not in visited:
                        visited.add(target)
                        new_queue.append(target)
            queue = new_queue
            height += 1
        return height

    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        adj_list = [list() for i in range(n)]
        for edge in edges:
            adj_list[edge[0]].append(edge[1])
            adj_list[edge[1]].append(edge[0])
        heights = [0 for i in range(n)]
        for i in range(n):
            heights[i] = self.getHeight(n, adj_list, i)
        min_height = min(heights)
        res = []
        for i, height in enumerate(heights):
            if height == min_height:
                res.append(i)
        return res