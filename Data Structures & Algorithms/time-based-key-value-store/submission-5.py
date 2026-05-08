class TimeMap:

    def __init__(self):
        self.timeMap = defaultdict(list) # key : [timestamp, val]

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timeMap[key].append([timestamp, value])
        return 

    def get(self, key: str, timestamp: int) -> str:

        if key not in self.timeMap:
            return ""
        res = ""
        l, r = 0 , len(self.timeMap[key])-1

        while l <= r:
            mid = l + (r-l)//2

            if self.timeMap[key][mid][0] <= timestamp:
                res = self.timeMap[key][mid][1]
                l = mid + 1
            else:
                r = mid - 1
        
        return res
