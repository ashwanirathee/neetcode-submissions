class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for i in strs:
            res += str(len(i))+"#"+i
        return res

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        while i < len(s):
            j = i
            while s[j]!= "#":
                j+=1
            length_of_string = int(s[i:j])
            # print(length_of_string)
            actual_string = s[j+1:j+1+length_of_string]
            result.append(actual_string)
            i = j + 1 + length_of_string
        return result