class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return -1

        mid = len(nums) // 2
        res = nums[mid]

        if target > res:
            ans = self.search(nums[mid+1:], target)

            if ans == -1:
                return -1

            return mid + 1 + ans

        elif target < res:
            return self.search(nums[:mid], target)

        else:
            return mid