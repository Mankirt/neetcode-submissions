class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        for i, s in enumerate(speed):
            position[i] = [position[i], s]
        position.sort()
        ans = 0
        t = 0
        for i in range(len(position)-1,-1,-1):
            new_time = (target - position[i][0])/position[i][1]
            if new_time > t:
                ans += 1
                t = new_time
        
        return ans