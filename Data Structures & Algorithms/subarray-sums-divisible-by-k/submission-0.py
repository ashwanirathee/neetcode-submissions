class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prefix_sum = [0] * (n+1)
        for i in range(1, n+1):
            prefix_sum[i] = prefix_sum[i-1] + nums[i-1]
        print(prefix_sum)
        count=0
        for i in range(n):
            for j in range(i + 1, n + 1):
                if (prefix_sum[j] - prefix_sum[i]) % k == 0:
                    count += 1

        return count