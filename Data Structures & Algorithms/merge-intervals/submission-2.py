class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        crr = intervals[0]
        ans = []
        for i in range(1,len(intervals)):
            if crr[1] < intervals[i][0]:
                ans.append(crr)
                crr = intervals[i]
            else:
                crr[1] = max(crr[1],intervals[i][1])
        
        ans.append(crr)
        return ans