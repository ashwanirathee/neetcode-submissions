class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        freq = {}
        for i in arr:
            freq[i] = freq.get(i, 0) + 1

        for i in arr:
            if freq[i] == 1:
                k-=1
                if k == 0:
                    return i

        return ""