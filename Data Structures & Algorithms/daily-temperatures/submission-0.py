class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)
        for idx, temp in enumerate(temperatures):
            if len(stack)==0 or temp < stack[-1][0]:
                stack.append((temp, idx))
                # print("appended:", stack)
            else:
                # print("other case w idx:", idx)
                while(len(stack) and temp > stack[-1][0]):
                    val = stack.pop()
                    # print("popped:", val)
                    res[val[1]] = idx - val[1]
                stack.append((temp, idx))
                # stack.append(temp)
        return res