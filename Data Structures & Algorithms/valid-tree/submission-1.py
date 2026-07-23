class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        al = {i: [] for i in range(n)}

        for p, q in edges:
            al[p].append(q)
            al[q].append(p)

        visited = [False] * n

        def dfs(s, parent):
            visited[s] = True

            for u in al[s]:
                if not visited[u]:
                    if not dfs(u, s):
                        return False
                elif u != parent:
                    return False

            return True

        if not dfs(0, -1):
            return False

        return all(visited)