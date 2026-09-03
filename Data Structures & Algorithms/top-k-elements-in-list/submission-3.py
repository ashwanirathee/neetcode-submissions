class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = Counter(nums)
        n = len(nums)
        freq_map_rev = [[] for i in range(n+1)]
        for num, cnt in freq_map.items():
            freq_map_rev[cnt].append(num)

        res = []
        for i in range(len(freq_map_rev) - 1, 0, -1):
            for num in freq_map_rev[i]:
                res.append(num)
                if len(res) == k:
                    return res