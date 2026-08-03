class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        adj_list = {}
        for i in range(1, n+1):
            adj_list[i] = []
        for i in trust:
                adj_list[i[0]].append(i[1])

        for p1 in adj_list:
            # is p1 judge?
            if len(adj_list[p1]) != 0:
                continue

            is_judge = True
            for p2 in adj_list:
                if p2 == p1:
                    continue
                if p1 not in adj_list[p2]:
                    is_judge=False

            if is_judge == True:
                return p1

        return -1