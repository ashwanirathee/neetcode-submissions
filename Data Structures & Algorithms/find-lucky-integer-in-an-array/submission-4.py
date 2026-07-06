class Solution:
    def findLucky(self, arr: List[int]) -> int:
        freq = {}
        for i in arr:
            freq[i] = freq.get(i, 0) + 1

        max_curr = -1
        for key in freq.keys():
            if freq[key] == key:
                max_curr = max(max_curr, key)

        return max_curr