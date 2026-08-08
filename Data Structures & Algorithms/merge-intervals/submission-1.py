class Solution:
    def merge(self, intervals):
        intervals.sort()

        c_l, c_r = intervals[0]
        res = []

        for n_l, n_r in intervals[1:]:
            if n_l <= c_r:
                c_r = max(c_r, n_r)
            else:
                res.append([c_l, c_r])
                c_l, c_r = n_l, n_r

        res.append([c_l, c_r])
        return res