class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float("inf") for i in range(n)]
        prices[src] = 0

        # iterate k+1 times
        for i in range(k+1):
            tempPrices = [float("inf") for i in range(n)]
            tempPrices[src] = 0
            # src, dest, price
            for s, d, p in flights:
                if prices[s] == float("inf"):
                    # we don't want to continue as it's unreachable 
                    continue
                if prices[s] + p < tempPrices[d]:
                    tempPrices[d] = prices[s] + p
            
            prices = tempPrices
        return -1 if prices[dst] == float("inf") else prices[dst]
