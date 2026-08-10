class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d = dict()
        for i in s:
            if i in d.keys():
                d[i]+=1
            else:
                d[i] = 1
        for i in t:
            if i in d.keys():
                d[i]-=1
            else:
                d[i] = 1
        for i in d.keys():
            if d[i] > 0:
                return False
        return True