class Solution:
    def dfs(self, grid, i, j, r, c):
        if i not in range(r) or j not in range(c):
            return

        if grid[i][j] == "0":
            return
        else:
            grid[i][j] = "0"
            self.dfs(grid, i+1, j, r, c)
            self.dfs(grid, i-1, j, r, c)
            self.dfs(grid, i, j+1, r, c)
            self.dfs(grid, i, j-1, r, c)

    def dfs_g(self, grid):
        r = len(grid)
        c = len(grid[0])
        count = 0
        for i in range(r):
            for j in range(c):
                if grid[i][j] == "1":
                    count += 1
                    self.dfs(grid, i, j, r, c)
        
        return count

    def numIslands(self, grid: List[List[str]]) -> int:
        count = self.dfs_g(grid)
        return count