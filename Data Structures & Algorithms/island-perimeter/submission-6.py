class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        n = [[-1, 0], [0, 1], [0, -1], [1, 0]]
        visited = set()
        def dfs(i, j, r, c):
            print(i, j)
            if (i,j) in visited:
                return 0
            visited.add((i,j))
            perimeter = 4

            for p, q in n:
                ni = i + p
                nj = j + q

                if (0 <= ni < rows and 0 <= nj < cols) and grid[ni][nj] == 1:
                    perimeter -=1
                    if (ni,nj) not in visited:
                        perimeter += dfs(ni, nj, r, c)


            return perimeter

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    res = dfs(i, j, rows, cols)
                    return res
        return 0
