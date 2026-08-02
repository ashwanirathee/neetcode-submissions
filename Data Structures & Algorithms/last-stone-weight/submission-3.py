class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)
        print(stones)
        while len(stones) > 1:
            a= heapq.heappop_max(stones)
            b= heapq.heappop_max(stones)
            if a !=b:
                heapq.heappush_max(stones, abs(a-b))
        
        if len(stones)!=0:
            return stones[0]
        return 0