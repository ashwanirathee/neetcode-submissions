class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        s, e = newInterval

        res = []
        i = 0
        n = len(intervals)
        while i < n and intervals[i][1] < s:
            res.append(intervals[i])
            i += 1
        # print(res)

        while i < n and intervals[i][0] <= e:
            nw = intervals[i]
            s = min(s, nw[0])
            e = max(e, nw[1])
            i += 1
        res.append([s,e])
        # print(res)

        while i < n:
            res.append(intervals[i])
            i += 1

        return res
            