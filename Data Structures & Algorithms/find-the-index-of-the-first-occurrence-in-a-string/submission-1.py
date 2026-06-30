class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        idx_res = 0
        for idx, i in enumerate(haystack):
            if i == needle[0]:
                idx_res = idx
                good = True
                for idxj, j in enumerate(needle):
                    if (idx_res + idxj > len(haystack)-1) or (j != haystack[idx_res + idxj]):
                        good= False
                        break
                if good:
                    return idx_res

        return -1