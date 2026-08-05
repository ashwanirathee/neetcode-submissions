class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        timemap = [[-1] * cols for _ in range(rows)]
        dirs = [[-1,0],[1,0],[0,1],[0,-1]]
        def bfs(q):
            # visited = set()
            time = 0
            while q:
                new_queue = []
                for el in q:
                    curr = el
                    i, j = curr
                    timemap[i][j] = time
                    for m, n in dirs:
                        ni = i + m
                        nj = j + n
                        if 0 <= ni < rows and 0 <= nj < cols and timemap[ni][nj] > time + 1:
                            timemap[ni][nj] = time + 1
                            new_queue.append((ni,nj))

                q = new_queue
                time += 1

        queue = deque([])
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    queue.append((i,j))
                    timemap[i][j] = 0

                if grid[i][j] == 1:
                    timemap[i][j] = float("inf")
                    
        bfs(queue)
        res = 0

        for row in timemap:
            for time in row:
                if time == float("inf"):
                    return -1

                if time != -1:
                    res = max(res, time)

        return res

    