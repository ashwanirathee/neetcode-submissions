class Solution:
    def bfs(self, grid, i, j):
        # print("bfs:", i, j)
        if i < 0 or i >= len(grid) or j<0 or j>=len(grid[0]):
            return 

        if grid[i][j]=="0":
            return 
        else:
            grid[i][j] = "0" 
            self.bfs(grid, i - 1, j)
            self.bfs(grid, i+1,j)
            self.bfs(grid, i, j-1)
            self.bfs(grid, i, j+1)

    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                # print(i,j, grid[i][j])
                if grid[i][j] == "1":
                    self.bfs(grid, i, j)
                    count +=1

        return count
