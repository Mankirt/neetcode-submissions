class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        d = {}
        for i,v in enumerate(position):
            d[v] = speed[i]
        position.sort()
        ans = 1
        last_time = (target-position[-1])/d[position[-1]]
        for i in range(len(position)-2,-1,-1):
            new_time = (target-position[i])/d[position[i]]
            if new_time > last_time:
                last_time = new_time
                ans+=1
        return ans
