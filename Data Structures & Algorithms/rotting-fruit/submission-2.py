class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        dist = [
            [float("inf") for _ in range(cols)]
            for _ in range(rows)
        ]

        def bfs(grid, i, j):
            queue = [(i, j)]
            visited = {(i, j)}

            dist[i][j] = 0

            neighbors = [
                [-1, 0],
                [1, 0],
                [0, -1],
                [0, 1],
            ]

            while queue:
                curr = queue.pop(0)
                i, j = curr

                for p, q in neighbors:
                    ni = i + p
                    nj = j + q

                    if ni not in range(rows) or nj not in range(cols):
                        continue

                    if (
                        (ni, nj) not in visited
                        and grid[ni][nj] > 0
                    ):
                        visited.add((ni, nj))

                        dist[ni][nj] = min(
                            dist[ni][nj],
                            dist[i][j] + 1,
                        )

                        queue.append((ni, nj))

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    bfs(grid, i, j)

        answer = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    if dist[i][j] == float("inf"):
                        return -1

                    answer = max(answer, dist[i][j])

        return answer