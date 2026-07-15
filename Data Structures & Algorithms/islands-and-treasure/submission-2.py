class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows = len(grid)
        cols = len(grid[0])

        def dfs(grid, i, j):
            if i < 0 or i >= rows or j < 0 or j >= cols:
                return -1
            
            print(grid[i][j], i, j)
            if grid[i][j] == -1:
                return -1
            else:
                if grid[i][j] == 0:
                    return 1
                else:
                    a = dfs(grid, i+1, j)
                    b = dfs(grid, i-1, j)
                    c = dfs(grid, i, j+1)
                    d = dfs(grid, i, j-1)
                    return min(a, b, c, d) + 1
    
        def bfs(grid, i, j):
            queue = [(i,j)]
            visited = {}
            neighbor = [[-1,0],[1,0], [0,-1], [0,1]]
            depth = 0
            while queue:
                curr = queue[0]
                queue.pop(0)
                visited[curr] = True
                i,j = curr
                print(curr)
                for p,q in neighbor:
                    ni = i + p
                    nj = j + q
                    if ni not in range(rows) or nj not in range(cols):
                        continue
                    if (ni, nj) not in visited and grid[ni][nj] > 0:
                        grid[ni][nj] = min(grid[i][j] + 1, grid[ni][nj])
                        queue.append((ni, nj))

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    print("new")
                    bfs(grid, i, j)
