class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        non_zero_count = 0
        for idx, i in enumerate(nums):
            if i > 0:
                nums[non_zero_count] = i
                non_zero_count+=1

        for idx in range(non_zero_count, len(nums)):
            nums[idx] = 0
        # print(non_zero_count, nums)
                
        