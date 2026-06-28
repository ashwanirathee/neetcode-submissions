class Solution:
    def dfs(self, grid, i, j):
        # print("idx:", i, j)
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
            return 0

        if grid[i][j] == 0:
            return 0
        else:
            grid[i][j] = 0
            area = 1 
            # print("before:", area)
            area += self.dfs(grid, i-1, j) # 0
            area += self.dfs(grid, i+1, j) # 1
            area += self.dfs(grid, i, j-1) # 0
            area += self.dfs(grid, i, j+1) # 0
            # print("after:", area)
            return area

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    # print(i, j)
                    area = self.dfs(grid, i, j)
                    # print(area)
                    max_area = max(area, max_area)

        return max_area