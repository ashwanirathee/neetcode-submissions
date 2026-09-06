class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [1] * n

        prefix_mult = 1
        for i in range(n):
            output[i] *= prefix_mult
            prefix_mult *= nums[i]


        suffix_mult = 1
        for i in reversed(range(n)):
            output[i] *= suffix_mult
            suffix_mult *= nums[i]
        
        return output