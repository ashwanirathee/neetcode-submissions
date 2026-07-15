class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def bfs(i):
            queue = [[0, []]]
            visited = {}

            subset = []
            while queue:
                curr = queue[0]
                queue.pop(0)

                sum_l = sum(curr[1])
                if sum_l > target:
                    continue

                # print(curr.val)
                if curr[0] == len(nums):
                    print(curr)
                    if sum(curr[1]) == target:
                        res.append(curr[1])
                    continue

                queue.append([curr[0], curr[1] + [nums[curr[0]]]])

                queue.append([curr[0] + 1, curr[1]])

        bfs(0)
        return res