class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        pac, atl = set(), set()

        n = [[-1, 0], [1, 0], [0, 1], [0, -1]]

        def dfs(i, j, s):
            if (i, j) in s:
                return
            s.add((i, j))

            for p, q in n:
                ni, nj = i + p, j + q
                if 0 <= ni < rows and 0 <= nj < cols and heights[ni][nj] >= heights[i][j]:
                    dfs(ni, nj, s)

        for i in range(cols):
            dfs(0, i, pac)
            dfs(rows - 1, i, atl)

        for i in range(rows):
            dfs(i, 0, pac)
            dfs(i, cols - 1, atl)

        return [[i, j] for i, j in pac & atl]
