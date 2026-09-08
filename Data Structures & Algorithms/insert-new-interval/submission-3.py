class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        new_start = newInterval[0]
        new_end = newInterval[1]
        ans = []
        i = 0
        while i < len(intervals):
            start = intervals[i][0]
            end = intervals[i][1]
            if start > new_end:
                ans.append([new_start,new_end])
                break
            if new_start <= end:
                new_start = min(start,new_start)
                new_end = max(new_end, end)
            else:
                ans.append([start,end])
            i += 1
        else:
            ans.append([new_start,new_end])
        ans.extend(intervals[i:])
        return ans