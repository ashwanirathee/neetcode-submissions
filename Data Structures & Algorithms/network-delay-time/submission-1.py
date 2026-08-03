class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        dist = [float("inf")] * (n + 1)
        dist[k] = 0

        for _ in range(n - 1):
            changed = False

            for u, v, w in times:
                if dist[u] != float("inf") and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    changed = True

            # No updates means shortest distances are finalized.
            if not changed:
                break

        answer = max(dist[1:])
        return answer if answer != float("inf") else -1