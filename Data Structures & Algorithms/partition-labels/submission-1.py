class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lpos = {c:i for i,c in enumerate(s)}
        ret = []
        l = 0
        b = 0
        for r in range(len(s)):
            b = max(b, lpos[s[r]])
            if b == r:
                ret.append(r-l+1)
                l = r + 1
        return ret
