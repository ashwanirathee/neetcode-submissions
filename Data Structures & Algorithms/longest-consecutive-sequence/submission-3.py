class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        nums.sort()
        cache = dict()
        for num in nums:
            print(num)
            if num-1 in cache.keys():
                cache[num] = cache[num-1]+1
            else:
                cache[num] = 1
        
        return max(list(cache.values()))