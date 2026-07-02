class Solution:
    def isPrefixAndSuffix(self,str1, str2):
        n1 = len(str1)
        n2 = len(str2)
        if str2[:n1] == str1 and str2[-n1:] == str1:
            return True

    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        res = 0
        n = len(words)
        for i in range(n):
            for j in range(i+1, n):
                if self.isPrefixAndSuffix(words[i], words[j]):
                    res+=1
        return res