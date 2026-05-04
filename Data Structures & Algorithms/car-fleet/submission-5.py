class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        x = [i for i in zip(position,speed)]
        x.sort(key = lambda x : x[0] )
        fleet = 0
        stack = [0]
        for i in range(len(x)-1,-1,-1):
            y = (target-x[i][0])/x[i][1]
            if stack[-1] < y:
                stack.append(y)
        
        return len(stack) - 1
            
        