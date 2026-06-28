class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        # print(nums)
        min_val = 100001
        for i in range(len(nums)-k+1):
            curr = nums[i+k-1]- nums[i]
            min_val = min(curr, min_val)
            # print(i, min_val, curr, nums[i+k-1], nums[i])
        return min_val

