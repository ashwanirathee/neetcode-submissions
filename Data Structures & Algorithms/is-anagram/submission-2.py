class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        cache = {}
        for char in s:
            # print(char, cache)
            if char in cache.keys():
                cache[char] += 1
            else:
                cache[char] = 1

        # print(cache)

        for char in t:
            if char in cache.keys():
                cache[char] -= 1
            else:
                # print("Early return")
                return False

        # print(cache)

        for key, value in cache.items():
            if value != 0:
                return False
            
        return True
        