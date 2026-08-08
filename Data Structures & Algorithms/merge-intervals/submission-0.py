class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])
        c_l, c_r = intervals[0]
        res = []

        n = len(intervals)
        for idx in range(1, n):
            n_l, n_r = intervals[idx]
            if c_l <= n_l <= c_r:
                c_l = min(n_l, c_l)
                c_r = max(n_r, c_r)
            else:
                res.append([c_l, c_r])
                c_l = n_l
                c_r = n_r
        res.append([c_l, c_r])
        return res