class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r = max(weights), sum(weights)
        res = r
        while l <= r:
            mid = (l+r) // 2
            # print("capacity:", mid)
            time = 0
            # for i in piles:
            #     time += ceil(float(i)/mid)
            our_days = 0
            curr_cap = mid
            for idx, weight in enumerate(weights):
                curr_cap = curr_cap - weight
                if curr_cap < 0:
                    our_days +=1
                    curr_cap = mid - weight
            # print(our_days, l, r, mid)

            if our_days < days:
                res = mid
                r = mid -1
            else:
                l = mid + 1

        return res
            