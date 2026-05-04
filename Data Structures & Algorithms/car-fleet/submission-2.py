class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        res=len(position)
        d={}
        for i,v in enumerate(position):
            d[v]=i
        position.sort()
        last_time= (target-position[-1])/speed[d[position[-1]]]
        p=last_time*position[-1]
        print(last_time)
        
        for i in range(len(position)-2,-1,-1):
            new_time=(target-position[i])/speed[d[position[i]]]
            if new_time>last_time:
                last_time = new_time
                print(last_time)
            else:
                res-=1
        return res