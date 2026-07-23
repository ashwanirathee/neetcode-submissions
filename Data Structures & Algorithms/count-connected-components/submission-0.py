class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        n = n
        numCourses = n
        V = list(range(numCourses))
        al = {i: [] for i in range(numCourses)}
        for p, q in edges:
            al[q].append(p)
            al[p].append(q)

        visited = [False] * n
        disc = [0] * n
        finish = [0] * n
        pred = [0] * n
        active = [False] * n
        time = 0

        def dfs(s):
            nonlocal visited, time
            visited[s] = True
            for u in al[s]:
                if visited[u] == False:
                    visited[u] = True
                    dfs(u)
            
        count = 0

        def dfs_g():
            nonlocal time, count
            for s in V:
                if visited[s] == False:
                    count += 1
                    dfs(s)

        dfs_g()
        return count
