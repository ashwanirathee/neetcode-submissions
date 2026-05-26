class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        res = [x for x in zip(position, speed)]
        res = sorted(res, key=lambda x: x[0], reverse=True)
        # print(res)
        stack = []
        for pos_speed in res:
            # print(pos_speed)
            time = int(target-pos_speed[0])/pos_speed[1]
            if len(stack) == 0 or time > stack[-1]:
                stack.append(time)
                
            # print(stack)
        return len(stack)