class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        prefix_mult = [1]
        for num in nums:
            prefix_mult.append(prefix_mult[-1] * num)

        suffix_mult = [1]
        for num in reversed(nums):
            suffix_mult.append(suffix_mult[-1] * num)

        suffix_mult.reverse()

        result = []

        for i in range(n):
            result.append(prefix_mult[i] * suffix_mult[i + 1])

        return result
