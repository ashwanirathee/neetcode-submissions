class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        eod = float(len(s)) // 2
        for idx, i in enumerate(s):
            # print(eod, idx)
            if idx < eod:
                temp = s[len(s)-idx-1]
                # print("idx last:", len(s)-idx-1)
                s[len(s)-idx-1] = s[idx]
                s[idx] = temp
            else:
                # print("no change")
                break
            # print(s)
        return s            