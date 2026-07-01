class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        last_count = 0
        size_count = 0
        for idx, i in enumerate(s):
            if i.isalpha():
                size_count +=1
            else:
                if size_count > 0:
                    last_count = size_count
                size_count = 0

        return last_count if size_count == 0 else size_count