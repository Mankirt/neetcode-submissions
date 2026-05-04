class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key = lambda x:x[1])
        s =[]
        e = []
        for trip in trips:
            s.append([trip[1],trip[0]])
            e.append([trip[2],trip[0]])
        
        i = 0
        j = 0

        while j <len(e):
            if i < len(s):
                if  s[i][0] < e[j][0]:
                    capacity -= s[i][1]
                    i+=1
                    
                elif s[i][0] > e[j][0]:
                    capacity += e[j][1]
                    j+=1
                else:
                    capacity -= s[i][1]
                    capacity += e[j][1]
                    i+=1
                    j+=1
            else:
                capacity += e[j][1]
                j+=1

            if capacity < 0 : return False
        return True

