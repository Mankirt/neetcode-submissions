class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ans = []
        i = 0
        while i <len(intervals):
            crr = intervals[i]
            if newInterval[1] < crr[0]:
                ans.append(newInterval)
                ans+=intervals[i:]
                return ans
            elif crr[1] < newInterval[0]:
                ans.append(crr)
            else:
                newInterval = ([min(newInterval[0],crr[0]),max(newInterval[1],crr[1])])
            i+=1 
        ans.append(newInterval)
        return ans
            
        
        
