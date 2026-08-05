class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = {}
        adj_list = {i: [] for i in range(numCourses)}
        for u, v in prerequisites:
            adj_list[u].append(v)

        visited = set()
        state = [0] * numCourses

        def dfs(u):
            nonlocal visited
            visited.add(u)
            state[u] = 1

            for v in adj_list[u]:
                if state[v] == 1:
                    return False

                if v not in visited:
                    res = dfs(v)
                    if res == False:
                        return False
            state[u] = 2
            return True

        for u in range(numCourses):
            if not dfs(u):
                return False

        return True
