class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLWRC = 0
        u_set = set()
        l = 0 
        r = 0
        for idx, ch in enumerate(s):
            print(maxLWRC, u_set)
            if ch in u_set:
                while s[l] != ch:
                    print("no", s[l], ch)
                    u_set.remove(s[l])
                    print(u_set, s[l])
                    l+=1
                l+=1
                if l > r:
                    r = l
                print("exists:", l, r, u_set)
            else:
                if len(u_set) == 0:
                    l = idx
                r = idx
                u_set.add(ch)

                print("not exists:", l, r, u_set)
            maxLWRC = max(maxLWRC, len(u_set))
        return maxLWRC