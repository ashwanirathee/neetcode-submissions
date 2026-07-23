class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        n = numCourses
        V = list(range(numCourses))
        al = {i: [] for i in range(numCourses)}
        for p, q in prerequisites:
            al[q].append(p)

        visited = [False] * n
        disc = [0] * n
        finish = [0] * n
        pred = [0] * n
        active = [False] * n
        time = 0

        def dfs(s):
            nonlocal visited, time
            visited[s] = True
            disc[s] = time
            active[s] = True
            time += 1
            for u in al[s]:
                if visited[u] == False:
                    visited[u] = True
                    pred[u] = s
                    if not dfs(u):
                        return False
                elif active[u]:
                    # Back edge: cycle found
                    return False
            active[s] = False
            finish[s] = time
            time += 1

            return True

        def dfs_g():
            nonlocal time
            for s in V:
                if visited[s] == False:
                    if not dfs(s):
                        return False
            return True

        return dfs_g()
