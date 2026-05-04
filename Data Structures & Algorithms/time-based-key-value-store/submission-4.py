class TimeMap:

    def __init__(self):
        self.d = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.d[key].append([value,timestamp])
        return

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.d:
            return ""
        arr = self.d[key]
        l = 0
        r = len(arr) - 1
        res = ""
        while l <= r:
            m = l + (r-l)//2
            if arr[m][1] == timestamp:
                return arr[m][0]
            elif arr[m][1] < timestamp:
                res = arr[m][0]
                l = m +1
            else:
                r = m - 1
        return res

