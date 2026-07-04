class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        one_count = 0
        for i in s:
            if i == '1':
                one_count+=1

        res = ["0"] * len(s)
        res[-1] = '1'
        one_count -=1

        for idx in range(len(res)):
            if one_count > 0:
                res[idx] = '1'
                one_count -=1
        return ''.join(res)
