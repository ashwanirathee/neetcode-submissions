class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def bfs(i):
            queue = [[0, []]]
            visited = {}

            subset = []
            while queue:
                curr = queue[0]
                queue.pop(0)

                # print(curr.val)
                if curr[0] == len(nums):
                    res.append(curr[1])
                    continue

                queue.append([curr[0] + 1, curr[1]])
                queue.append([curr[0] + 1, curr[1] + [nums[curr[0]]]])

        bfs(0)
        return res
