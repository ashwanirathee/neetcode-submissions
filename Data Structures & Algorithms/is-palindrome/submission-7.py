class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = len(s)
        l = 0
        r = n-1
        
        while l < r:
            if not s[r].isalnum():
                r-=1
                continue
            if not s[l].isalnum():
                l+=1
                continue

            print(s[l], s[r])

            # if l > r:
            #     return False

            if s[l].lower() == s[r].lower():
                l += 1
                r -= 1
            else:
                return False
        return True