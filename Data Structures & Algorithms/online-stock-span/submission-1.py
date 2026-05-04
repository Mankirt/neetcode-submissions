class StockSpanner:

    def __init__(self):
        self.st = []

    def next(self, price: int) -> int:
        total_days = 1
        while self.st and self.st[-1][0] <= price:
            val, days = self.st.pop()
            total_days += days
        self.st.append([price,total_days])
        return total_days


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)