class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        # print(nums)
        for i, num in enumerate(nums):
            if num > 0:
                break

            if i > 0 and nums[i] == nums[i-1]:
                continue

            rem = -num
            j = i + 1
            k = len(nums)-1
            while (j < k):
                # print(j, k)
                sum_jk = nums[j] + nums[k]
                if sum_jk == rem:
                    res.append([nums[i], nums[j], nums[k]])
                    # break
                    j+=1
                    k-=1
                    while nums[j] == nums[j - 1] and j < k:
                        j += 1
                elif sum_jk > rem:
                    k-=1
                elif sum_jk < rem:
                    j+=1

        return res