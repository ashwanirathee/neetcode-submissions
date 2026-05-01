class Solution:
    def isPalindrome(self, s: str) -> bool:
        stack = []
        
        for idx, i in enumerate(s):
            if i.isalnum() == False:
                continue
            stack.append(i.lower())

        for idx, i in enumerate(s):
            if i.isalnum() == False:
                continue
            if stack[-1] == i.lower():
                stack.pop()
            else:
                return False

        return True if len(stack) == 0 else 0