class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_mul = [1]
        for i in nums:
            prefix_mul.append(prefix_mul[-1] * i)
        print(prefix_mul)

        postfix_mul = [1]
        for i in reversed(nums):
            postfix_mul.append(postfix_mul[-1] * i)
        print(postfix_mul)

        res = []
        for idx, val in enumerate(nums):
            post_idx = len(postfix_mul)-2-idx
            print(post_idx)
            print(prefix_mul[idx], postfix_mul[post_idx])
            res.append(prefix_mul[idx] * postfix_mul[post_idx])
        return res