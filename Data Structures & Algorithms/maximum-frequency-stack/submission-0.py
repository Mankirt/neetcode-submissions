class FreqStack:

    def __init__(self):
        self.count = {}
        self.maxVal = 0
        self.stacks = {}
    def push(self, val: int) -> None:
        freq = self.count.get(val,0) + 1
        self.count[val] = freq
        self.maxVal = max(self.maxVal, freq)
        if self.maxVal not in self.stacks:
            self.stacks[self.maxVal] = []
        self.stacks[freq].append(val)

    def pop(self) -> int:
        res = self.stacks[self.maxVal].pop()
        self.count[res] -=1
        if not self.stacks[self.maxVal]:
            self.maxVal -= 1
        return res


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()