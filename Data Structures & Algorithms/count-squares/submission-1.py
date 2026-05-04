class CountSquares:

    def __init__(self):
        self.points = defaultdict(int)
        self.l_points = []

    def add(self, point: List[int]) -> None:
        self.points[tuple(point)] += 1
        self.l_points.append(point)

    def count(self, point: List[int]) -> int:
        res = 0
        for x,y in self.l_points:

            if [x,y] == point or abs(point[0]-x) != abs(point[1]-y):
                continue
            res += self.points[(x,point[1])] * self.points[(point[0],y)]

        return res

