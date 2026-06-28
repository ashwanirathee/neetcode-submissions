class Solution:
    def specialArray(self, nums: List[int]) -> int:
        for idx, i in enumerate(range(len(nums)+1)):
            # print(idx, i)

            count = 0
            for idx2, val in enumerate(nums):
                if val >= i:
                    count+=1

            # print(count, val)

            if count == i:
                return i
        return -1