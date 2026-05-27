class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return -1

        mid = len(nums) // 2
        curr_mid = nums[mid]

        if curr_mid < target:
            result = self.search(nums[mid+1:], target)
            if result == -1:
                return -1
            return mid + 1 + result
        elif curr_mid > target:
            return self.search(nums[:mid], target)
        else:
            return mid