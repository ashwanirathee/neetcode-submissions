class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        cache = {}
        for i in strs:
            si = "".join(sorted(i))
            if si in cache.keys():
                cache[si].append(i)
            else:
                cache[si] = [i]

        return list(cache.values())