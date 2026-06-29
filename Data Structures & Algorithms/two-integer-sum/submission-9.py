class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        cache = {}

        for idx, i in enumerate(nums):
            res = target - i
            if res in cache.keys():
                return [cache[res], idx]
            else:
                cache[i] = idx

        return [0,0]