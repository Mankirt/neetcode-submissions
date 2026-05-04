class MedianFinder:

    def __init__(self):
        self.left = []
        self.right = []

    def addNum(self, num: int) -> None:
        if not self.left and not self.right:
            heapq.heappush(self.left,-num)
            return
        if num <= (-self.left[0]):
            heapq.heappush(self.left,-num)
        else:
            heapq.heappush(self.right,num)

        if len(self.left) > len(self.right) + 1:
            heapq.heappush(self.right,-heapq.heappop(self.left))
        if len(self.right) > len(self.left) + 1:
            heapq.heappush(self.left,-heapq.heappop(self.right))
        return

    def findMedian(self) -> float:
        if len(self.left) > len(self.right):
            return -self.left[0]
        elif len(self.left) < len(self.right):
            return self.right[0]
        else:
            return (-self.left[0]+self.right[0])/2
        