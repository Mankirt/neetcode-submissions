class TimeMap:

    def __init__(self):
        self.d = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.d:
            self.d[key] = []
        self.d[key].append([value,timestamp])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.d:
            return ""
        l = 0
        r = len(self.d[key]) - 1
        res = ""
        while l <= r:
            m = l + (r-l)//2
            if self.d[key][m][1] == timestamp:
                return self.d[key][m][0]
            
            if self.d[key][m][1] < timestamp :
                res = self.d[key][m][0]
                l = m + 1
            else:
                r = m - 1
        
        return res
