class MyQueue:

    def __init__(self):
        self.st1 = []
        self.st2 = []

    def push(self, x: int) -> None:
        self.st1.append(x)

    def pop(self) -> int:
        if not self.st2:
            self.move()
        return self.st2.pop()

    def peek(self) -> int:
        if not self.st2:
            self.move()
        return self.st2[-1]
        

    def empty(self) -> bool:
        if len(self.st1)==0 and len(self.st2) ==0:
            return True
        return False
    
    def move(self):
        while self.st1:
            self.st2.append(self.st1.pop())


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()