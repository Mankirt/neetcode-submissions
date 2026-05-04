class CountSquares:

    def __init__(self):
        self.d = defaultdict(int)
        self.l = []

    def add(self, point: List[int]) -> None:
        self.d[tuple(point)]+=1
        self.l.append(point)

    def count(self, point: List[int]) -> int:
        res = 0
        x,y = point
        for x1,y1 in self.l:
            if (abs(x1-x) == abs(y1-y) and x1!=x):
                res += self.d[(x,y1)] * self.d[(x1,y)]
        return res
