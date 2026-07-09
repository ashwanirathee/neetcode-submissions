class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_count = 0
        cnt = 0
        for i in nums:
            if i == 1:
                cnt+=1
            else:
                cnt = 0

            max_count = max(max_count, cnt)
        return max_count