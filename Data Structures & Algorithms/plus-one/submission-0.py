class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        n = len(digits)
        for idx in range(n):
            curr = digits[n-idx-1]
            res = curr + carry
            if res >= 10:
                digits[n-idx-1] = res % 10
                carry = 1
            else:
                digits[n-idx-1] = res
                carry = 0
            print(carry)

        if carry == 1:
            res = [1]
            res.extend(digits)
            digits = res
        return digits