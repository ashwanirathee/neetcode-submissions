class Solution:
    def dfs(self, grid, i, j, r, c):
        if i not in range(r) or j not in range(c):
            return 0

        area = 0
        if grid[i][j] == 0:
            return 0
        else:
            grid[i][j] = 0
            area += 1
            area += self.dfs(grid, i+1, j, r, c)
            area += self.dfs(grid, i-1, j, r, c)
            area += self.dfs(grid, i, j+1, r, c)
            area += self.dfs(grid, i, j-1, r, c)

        return area

    def dfs_g(self, grid):
        r = len(grid)
        c = len(grid[0])
        count = 0
        max_area = 0
        for i in range(r):
            for j in range(c):
                if grid[i][j] == 1:
                    count += 1
                    max_area = max(max_area, self.dfs(grid, i, j, r, c))
        
        return max_area

    def maxAreaOfIsland(self, grid: List[List[str]]) -> int:
        count = self.dfs_g(grid)
        return count