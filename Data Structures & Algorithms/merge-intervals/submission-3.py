class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        st = intervals[0][0]
        end = intervals[0][1]
        ans = []
        for x , y in intervals[1:]:
            if x > end:
                ans.append([st,end])
                st = x
                end = y
            else:
                end = max(end,y)
        
        ans.append([st,end])
        return ans