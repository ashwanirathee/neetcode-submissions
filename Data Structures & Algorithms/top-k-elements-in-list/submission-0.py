class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cache = {}
        for i in nums:
            if i in cache.keys():
                cache[i] +=1
            else:
                cache[i] = 1

        reduced = [[key, val] for key, val in cache.items()]

        reduced = sorted(reduced, key=lambda x: x[1], reverse=True)

        result = []
        for i in reduced:
            result.append(i[0])
            if len(result) == k:
                break
        
        return result