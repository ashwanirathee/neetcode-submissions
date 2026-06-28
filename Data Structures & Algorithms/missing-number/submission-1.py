class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = set(nums)
        full = set(list(range(len(nums)+1)))
        rem = full-res
        return rem.pop()