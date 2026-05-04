class FreqStack:

    def __init__(self):
        self.count = defaultdict(list)
        self.maxc = 0
        self.freq = defaultdict(int)

    def push(self, val: int) -> None:
        self.freq[val] += 1
        self.count[self.freq[val]].append(val)
        self.maxc = max(self.maxc, self.freq[val])
        return

    def pop(self) -> int:
        val = self.count[self.maxc].pop()
        self.freq[val] -=1
        if len(self.count[self.maxc]) == 0:
            self.maxc -=1
        return val


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()