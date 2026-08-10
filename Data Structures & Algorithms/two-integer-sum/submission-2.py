class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, initial in enumerate(nums):
            for j, new in enumerate(nums[i + 1:], start=i + 1):
                if initial + new == target:
                    return [i, j]