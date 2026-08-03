class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])
        pac = [[False] * cols for _ in range(rows)]
        atl = [[False] * cols for _ in range(rows)]
        n = [[-1,0],[1,0],[0,1],[0,-1]]

        def dfs(i,j, r, c, oc):
            print(i,j)
            # if i in [0, r-1] or j in [0, c-1]:
            #     print("interesting")
            #     return 
            if oc[i][j]:
                return 
            oc[i][j] = True

            for p, q in n:
                ni = i + p
                nj = j + q
                if 0 <= ni < r and 0 <= nj < c and heights[i][j] <= heights[ni][nj]:
                    dfs(ni, nj, r, c, oc)


        for i in range(rows):
            print('new start')
            dfs(i, cols-1, rows, cols, pac)
            dfs(i, 0, rows, cols, atl)

        for j in range(cols):
            dfs(0, j, rows, cols, atl)
            dfs(rows-1, j, rows, cols, pac)

        res = []
        for i in range(rows):
            for j in range(cols):
                if pac[i][j] and atl[i][j]:
                    res.append([i,j])

        return res

