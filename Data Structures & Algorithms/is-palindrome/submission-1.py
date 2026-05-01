class Solution:
    def isPalindrome(self, s: str) -> bool:
        stack = []
        for idx, i in enumerate(s):
            if i.isalnum() == False:
                continue
            stack.append(i.lower())

        # print(stack)

        for idx, i in enumerate(s):
            if i.isalnum() == False:
                continue
            
            # print(stack, i)
            if stack[-1] == i.lower():
                stack.pop()
            else:
                return False
            # print(idx, i)
        return True if len(stack) == 0 else 0