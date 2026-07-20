class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        start_idx = 0
        max_sum = nums[start_idx]
        count = 1
        n = len(nums)
        for i in range(1, len(nums)):
            print(start_idx, count, max_sum)
            if nums[i] > nums[i-1]:
                count +=1
            else:
                start_idx = i
                count = 1
                # max_sum = nums[start_idx]
            
            max_sum = max(max_sum, sum(nums[start_idx:start_idx+count]))
            print(start_idx, count, max_sum)
        return max_sum