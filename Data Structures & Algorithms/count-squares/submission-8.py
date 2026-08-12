class CountSquares:

    def __init__(self):
        self.x_data = {}
        self.y_data = {}
        self.xy_data = {}

    def add(self, point: List[int]) -> None:
        x, y = point
        if x not in self.x_data:
            self.x_data[x] = [point]
        else:
            self.x_data[x].append(point)

        if y not in self.y_data:
            self.y_data[y] = [point]
        else:
            self.y_data[y].append(point)

        point = tuple(point)
        if point not in self.xy_data:
            self.xy_data[point] = 1
        else:
            self.xy_data[point] += 1

    def count(self, point: List[int]) -> int:
        # print(self.x_data)
        # print(self.y_data)
        x1, y1 = point
        count = 0 
        if x1 not in self.x_data or y1 not in self.y_data:
            return 0
        for x2, y2 in self.x_data[x1]:
            # print("Found some:", (x2,y2))
            if y2 == y1:
                continue

            for x3, y3 in self.y_data[y1]:
                # print((x1, y1), (x2, y2),(x3, y3))
                 # square condition
                if abs(y2 - y1) != abs(x3 - x1):
                    continue
                if (x3,y2) in self.xy_data:
                    count+=self.xy_data[(x3,y2)]
        return count