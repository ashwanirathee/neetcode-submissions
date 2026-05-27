class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers)-1
        # print(i, j)
        while(i<j):
            res = numbers[i] + numbers[j]
            if res == target:
                break
            elif res > target:
                j-=1
            elif res < target:
                i+=1
        return [i+1,j+1]