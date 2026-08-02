class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        dist = [float("inf")] * (n+1)
        dist[k] = 0
        visited = [False] * (n+1)
        adj_list = {}
        for ui, vi, ti in times:
            if ui in adj_list:
                adj_list[ui].append((vi, ti))
            else:
                adj_list[ui] = [(vi, ti)]


        minHeap = [(0,k)]
        while minHeap:
            weight, u = heapq.heappop(minHeap)
            if visited[u] == True:
                continue
            visited[u] = True
            if u not in adj_list:
                continue
            for v, w_new in adj_list[u]:
                if not visited[v] and dist[u] + w_new < dist[v]:
                    heapq.heappush(minHeap, (weight+w_new, v))
                    dist[v] = dist[u] + w_new
        return max(dist[1:]) if all(visited[1:]) else -1