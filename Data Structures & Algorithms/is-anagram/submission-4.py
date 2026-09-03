class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        fs = Counter(s)
        ft = Counter(t)
        return True if len(fs-ft) == 0 and len(ft-fs)==0 else False