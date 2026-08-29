class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        n = len(nums)

        prefix_sum = [0] * (n + 1) # indexable till n
        for i in range(1, n+1):
            # i indexable till n
            prefix_sum[i] = prefix_sum[i-1] + nums[i-1]

        # print(prefix_sum)

        res = 0
        # n-1 is last index
        for i in range(0, n):
            for j in range(i+1, n+1):
                # we start with i+1 as to include atleast one element and n+1 so that we can access data from prefix_sum appropriately
                if (prefix_sum[j]-prefix_sum[i]) % k == 0:
                    res+=1
        return res 