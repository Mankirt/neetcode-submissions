class MinStack:

    def __init__(self):
        self.stack = []
        self.temp = []


    def push(self, val: int) -> None:

        self.stack.append(val)
        if self.temp and self.temp[-1] < val:
                val = self.temp[-1]
        self.temp.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.temp.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.temp[-1]
