class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        inf = float("inf")
        A = [[inf] * (n + 1) for _ in range(n + 1)]
        for i in range(1, n + 1):
            A[i][i] = 0

        for u, v, w in times:
            A[u][v] = w

        for t in range(1, n + 1):
            for i in range(1, n + 1):
                for j in range(1, n + 1):
                    A[i][j] = min(A[i][j], A[i][t] + A[t][j])

        answer = max(A[k][1:])

        return answer if answer != inf else -1
