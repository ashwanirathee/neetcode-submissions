class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        i = -1
        j = -1
        typ = 0
        n = len(nums)
        idx = 0
        res = [0]*n
        while idx < n:
            if typ == 0:
                # needs to be positive
                i+=1
                while nums[i] < 0:
                    i+=1
                res[idx] = nums[i]
                typ = 1
            else:
                # type one 
                j+=1
                while nums[j] > 0:
                    j+=1
                res[idx] = nums[j]
                typ = 0
            idx += 1
        return res