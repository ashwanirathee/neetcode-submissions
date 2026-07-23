class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rm, cm = len(heights), len(heights[0])
        pc, al = set(), set()
        n = [[-1,0],[1,0],[0,1],[0,-1]]
        def dfs(i, j, s):
            if (i,j) in s:
                return
            
            s.add((i,j))
            for p,q in n:
                ni, nj = i + p, j + q
                if 0 <= ni < rm and 0 <= nj < cm and heights[ni][nj] >= heights[i][j]:
                    dfs(ni, nj, s)

        for i in range(rm):
            dfs(i, 0, pc)
            dfs(i, cm-1, al)
        
        for j in range(cm):
            dfs(0, j, pc)
            dfs(rm-1, j, al)


        return [[i,j] for i,j in pc & al]