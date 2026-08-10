class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = dict()
        for i, val in enumerate(nums):
            d[val] = i
        for i, val in enumerate(nums):
            print(val)
            if target-val in d.keys() and d[target-val] is not i:
                return [i, d[target-val]]