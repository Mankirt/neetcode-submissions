class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ans = []
        last_s = 0
        last_e = 0
        for i,interval in enumerate(intervals):
            if interval[0] > newInterval[1]:
                ans.append(newInterval)
                ans.extend(intervals[i:])
                return ans
            
            elif interval[1] >= newInterval[0]:
                
                newInterval[0] = min(interval[0], newInterval[0])
                newInterval[1] = max(interval[1],newInterval[1])
            
            else:
                ans.append(interval)
        ans.append(newInterval)
        return ans
