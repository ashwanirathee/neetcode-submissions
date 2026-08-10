class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        n = len(heights)
        res = [0] * n
        res[n-1] = 1 
        for i in range(n-1):
            a = heights[i+1:]
            print(i, a)
            res[i] = 1 if max(a) < heights[i] else 0

        output = []
        for i in range(n):
            if res[i] == 1:
                output.append(i)
        return output