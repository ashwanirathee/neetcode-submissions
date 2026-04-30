class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_mul = [1]
        for i in nums:
            prefix_mul.append(prefix_mul[-1] * i)

        postfix_mul = [1]
        for i in reversed(nums):
            postfix_mul.append(postfix_mul[-1] * i)

        res = []
        for idx, val in enumerate(nums):
            post_idx = len(postfix_mul)-2-idx
            res.append(prefix_mul[idx] * postfix_mul[post_idx])
        return res