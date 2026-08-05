class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        dirs = [[-1,0],[1,0],[0,1],[0,-1]]
        islands_count = 0
        global_visited = set()

        def bfs(i, j):
            nonlocal rows, cols
            local_visited = set()

            q = deque([(i,j)])
            while q:
                curr = q.popleft()
                local_visited.add(curr)
                print(curr)
                for m, n in dirs:
                    ni = curr[0] + m
                    nj = curr[1] + n
                    nw = (ni,nj)
                    if 0 <= ni < rows and 0<=nj < cols and nw not in local_visited and grid[ni][nj]=="1":
                        q.append(nw)
                


            return local_visited

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1" and (i, j) not in global_visited:
                    local_visited = bfs(i, j)
                    islands_count += 1
                    global_visited.update(local_visited)

        return islands_count