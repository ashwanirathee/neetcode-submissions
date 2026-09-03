class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        cmap = {}
        n = len(nums)

        for idx in range(n):
            res = target - nums[idx]
            if res in cmap:
                return [cmap[res], idx]
            else:
                cmap[nums[idx]] = idx
        return [0,0]