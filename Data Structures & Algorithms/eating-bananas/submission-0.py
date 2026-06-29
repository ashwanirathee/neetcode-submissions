class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r
        while l <= r:
            mid = (l+r) // 2
            time = 0
            for i in piles:
                time += math.ceil(float(i)/mid)

            if time <= h:
                res = mid
                r = mid -1
            else:
                l = mid + 1

        return res