class CountSquares:
    def __init__(self):
        self.data_list = {}
        self.x_list = {}
        self.y_list = {}

    def add(self, point: List[int]) -> None:
        key = tuple(point)
        if key in self.data_list:
            self.data_list[key] += 1
        else:
            self.data_list[key] = 1

        if key[0] in self.x_list:
            self.x_list[key[0]].append(key)
        else:
            self.x_list[key[0]] = [key]

        
        if key[1] in self.y_list:
            self.y_list[key[1]].append(key)
        else:
            self.y_list[key[1]] = [key]

    def count(self, point: List[int]) -> int:
        count = 0
        x1, y1 = point
        if x1 not in self.x_list or y1 not in self.y_list:
            return count
        for old_x in self.x_list[x1]:
            print(old_x)
            x2, y2 = old_x
            dist = abs(y2 - y1)
            if dist == 0:
                continue
            for old_y in self.y_list[y1]:
                x3, y3 = old_y
                dist2 = abs(x3-x1)
                if dist2 == dist:
                    print(old_x, old_y)
                    print((x2, y3), self.data_list)
                    if (x3, y2) in self.data_list:
                        print("here")
                        count += self.data_list[(x3, y2)]
        return count
