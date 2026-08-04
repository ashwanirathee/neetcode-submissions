class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        def dfs(i, j):
            nonlocal rows, cols
            if i < 0 or i == rows or j < 0 or j == cols:
                return -1, 0

            if grid[i][j] == 0:
                return 0, 0
            else:
                grid[i][j] = 0
                r1 = dfs(i + 1, j)
                r2 = dfs(i - 1, j)
                r3 = dfs(i, j - 1)
                r4 = dfs(i, j + 1)
            return min(r1[0], r2[0], r3[0], r4[0]), 1 + r1[1] + r2[1] + r3[1] + r4[1]

        count = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    res, l = dfs(i, j)
                    print(i, j, res, l)
                    if res != -1:
                        count += l

        return count
