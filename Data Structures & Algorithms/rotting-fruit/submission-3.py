class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        n = [[-1,0],[1,0],[0,1],[0,-1]]
        dist = [[-1]*cols for _ in range(rows)]
        def bfs(queue, dist):
            nonlocal rows, cols
            visited = set()
            time = 1
            while queue:
                new_queue = []
                for i,j in queue:
                    print("start:", i,j)
                    for p, q in n:
                        ni = i+p
                        nj = j+q
                        print()
                        if 0 <= ni < rows and 0 <= nj < cols and grid[ni][nj] == 1 and dist[ni][nj] > time:
                            new_queue.append([ni,nj])
                            dist[ni][nj] = time
                queue = new_queue
                time +=1 
            return dist
        queue = []
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    queue.append([i,j])
                    dist[i][j] = 0
                elif grid[i][j] == 1:
                    dist[i][j] = float("inf")
        dist = bfs(queue, dist)

        print(dist)
        answer = 0

        for i in range(rows):
            for j in range(cols):
                # A fresh orange was never reached.
                if dist[i][j] == float("inf"):
                    return -1

                # Ignore empty cells represented by -1.
                answer = max(answer, dist[i][j])

        return answer
