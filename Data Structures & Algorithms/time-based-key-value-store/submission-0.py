class TimeMap:

    def __init__(self):
        self.d=defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.d[key].append((timestamp,value))

    def get(self, key: str, timestamp: int) -> str:
        print(self.d[key])
        l=0
        r=len(self.d[key])-1
        res=""
        while l<=r:
            mid = l + (r-l)//2
            print(mid)
            print(timestamp , self.d[key][mid][0],self.d[key][mid][1])
            if timestamp == self.d[key][mid][0]:
                return self.d[key][mid][1]
            if timestamp > self.d[key][mid][0]:
                res=self.d[key][mid][1]
                l=mid+1
            else:
                r=mid-1
        return res
