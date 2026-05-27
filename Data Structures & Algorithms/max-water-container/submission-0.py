class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j=len(heights)-1
        maxArea = 0
        while(i < j):
            minHeight = min(heights[i], heights[j])
            maxArea = max(maxArea, (j-i)*minHeight)
            # print(maxArea)
            if heights[i] > heights[j]:
                j-=1
            elif heights[i] < heights[j]:
                i+=1
            else:
                i+=1
        return maxArea