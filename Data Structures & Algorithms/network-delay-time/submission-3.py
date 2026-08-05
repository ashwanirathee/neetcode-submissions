class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        dist = [float("inf")] * (n+1)
        dist[k] = 0

        adj_list = {}
        for i in range(1, n+1):
            adj_list[i] = []
        for ui,vi,ti in times:
            adj_list[ui].append([vi, ti])

        heap = [(0, k)]
        visited = set()
        while heap:
            weight, u = heapq.heappop(heap)
            if weight > dist[u]:
                continue
            # visited.add(u)
            for v, ti in adj_list[u]:
                if dist[u] + ti < dist[v]:
                    dist[v] = dist[u] + ti
                    heapq.heappush(heap, (dist[v], v))
                    
        answer = max(dist[1:])
        return -1 if answer == float("inf") else answer