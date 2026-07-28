class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        l = 0
        r = n - 1
        while l < r:
            # print(numbers[l] + numbers[r])
            # l+=1
            # r-=1
            p = numbers[l] + numbers[r]
            if p > target:
                r-=1
            elif p < target:
                l+=1
            else:
                return [l+1, r+1] 
        return [-1,-1]