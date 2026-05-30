class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLWRC = 0
        u_set = set()
        i = 0 
        j = 0
        for idx, ch in enumerate(s):
            print(maxLWRC, u_set)
            if ch in u_set:
                while s[i] != ch:
                    print("no", s[i], ch)
                    u_set.remove(s[i])
                    print(u_set, s[i])
                    i+=1
                i+=1
                if i > j:
                    j = i
                print("exists:", i, j, u_set)
            else:
                if len(u_set) == 0:
                    i = idx
                j = idx
                u_set.add(ch)

                print("not exists:", i, j, u_set)
            maxLWRC = max(maxLWRC, len(u_set))
        return maxLWRC