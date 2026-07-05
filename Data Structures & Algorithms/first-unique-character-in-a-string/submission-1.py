class Solution:
    def firstUniqChar(self, s: str) -> int:
        freq = {}
        for idx, i in enumerate(s):
            if i in freq.keys():
                freq[i].append(idx)
            else:
                freq[i] = [idx]
            # print(freq)

        for key in freq.keys():
            if len(freq[key]) == 1:
                return freq[key][0]
        return -1