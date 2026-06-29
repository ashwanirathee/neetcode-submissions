class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            j = i + 1
            for j in range(j, len(nums)):
                if nums[j] + nums[i] == target:
                    return [i, j]

        return [0,0]